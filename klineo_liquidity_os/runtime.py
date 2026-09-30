"""Standard-library HTTP transport shared by the generated operation methods."""
from __future__ import annotations

import base64
import http.client
import json
import math
import re
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Mapping
from typing import Callable, Optional, TypeAlias, Union, cast

ResponseObserver: TypeAlias = Callable[[int, Mapping[str, str]], None]


class LiquidityOsApiError(RuntimeError):
    """The API returned a non-success HTTP status."""

    def __init__(self, status: int, code: str, message: str, correlation_id: Optional[str] = None,
                 *, retry_after: Optional[str] = None, retryable: Optional[bool] = None,
                 remediation: Optional[str] = None, field_errors: Optional[Mapping[str, object]] = None):
        super().__init__(message)
        self.status = status
        self.code = code
        self.correlation_id = correlation_id
        self.retry_after = retry_after
        self.retryable = retryable
        self.remediation = remediation
        self.field_errors = field_errors


class LiquidityOsTransportError(RuntimeError):
    """The connection failed or timed out; mutation completion may be unknown."""


class LiquidityOsResponseError(RuntimeError):
    """A successful response did not contain the expected JSON representation."""


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Credentials and tenant headers must never follow redirects.
        return None


def _header(value: str, name: str) -> str:
    if not isinstance(value, str) or not value or any(ord(c) < 32 or ord(c) > 126 for c in value):
        raise ValueError(f"{name} must be a nonempty printable ASCII string")
    return value


class LiquidityOsTransport:
    base_url: str
    organization_id: Optional[str]
    access_token: Optional[str]
    timeout_seconds: float
    on_response: Optional[ResponseObserver]

    def __post_init__(self) -> None:
        if not isinstance(self.base_url, str) or not self.base_url or any(c.isspace() for c in self.base_url):
            raise ValueError("base_url must be an absolute HTTP(S) URL without whitespace")
        parsed = urllib.parse.urlsplit(self.base_url)
        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            raise ValueError("base_url must be an absolute HTTP(S) URL")
        if parsed.username is not None or parsed.password is not None or "?" in self.base_url or "#" in self.base_url or "\\" in self.base_url:
            raise ValueError("base_url must not contain credentials, a query, or a fragment")
        try:
            parsed.port
        except ValueError as error:
            raise ValueError("base_url contains an invalid port") from error
        if isinstance(self.timeout_seconds, bool) or not isinstance(self.timeout_seconds, (int, float)) or not math.isfinite(self.timeout_seconds) or self.timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be a finite positive number")
        if self.organization_id is not None:
            _header(self.organization_id, "organization_id")
        if self.access_token is not None:
            _header(self.access_token, "access_token")
        if self.on_response is not None and not callable(self.on_response):
            raise ValueError("on_response must be callable")

    def _request(self, method: str, template: str, *, path: Optional[Mapping[str, Union[str, int]]] = None,
                 query: Optional[Mapping[str, Union[str, int, bool]]] = None, body: Optional[object] = None,
                 if_match: Optional[str] = None, idempotency_key: Optional[str] = None,
                 basic_auth: Optional[tuple[str, str]] = None, content_type: Optional[str] = None,
                 accept: str = "application/json") -> object:
        rendered = template
        required = set(re.findall(r"\{([^}]+)\}", template))
        if path is not None and not isinstance(path, Mapping):
            raise ValueError("path must be a mapping")
        if set(path or {}) != required:
            raise ValueError("Path parameters must exactly match the operation")
        for name, value in (path or {}).items():
            if isinstance(value, bool) or not isinstance(value, (str, int)) or not str(value) or str(value) in (".", ".."):
                raise ValueError(f"Invalid path parameter: {name}")
            rendered = rendered.replace("{" + name + "}", urllib.parse.quote(str(value), safe=""))
        url = self.base_url.rstrip("/") + rendered
        if query is not None:
            if not isinstance(query, Mapping) or any(not isinstance(name, str) or not isinstance(value, (str, int, bool, type(None))) for name, value in query.items()):
                raise ValueError("query must map strings to strings, integers, booleans, or None")
            encoded_query = urllib.parse.urlencode({name: str(value).lower() if isinstance(value, bool) else value for name, value in query.items() if value is not None})
            if encoded_query:
                url += "?" + encoded_query
        headers = {"Accept": accept}
        if self.organization_id is not None:
            headers["x-klineo-organization-id"] = self.organization_id
        if self.access_token is not None:
            headers["Authorization"] = "Bearer " + self.access_token
        if basic_auth is not None:
            if len(basic_auth) != 2 or any(not isinstance(value, str) or not value for value in basic_auth):
                raise ValueError("OAuth client ID and secret must be nonempty strings")
            credentials = ":".join(urllib.parse.quote_plus(value, safe="") for value in basic_auth).encode("utf-8")
            headers["Authorization"] = "Basic " + base64.b64encode(credentials).decode("ascii")
        if if_match is not None:
            value = _header(if_match, "if_match")
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            if not value or '"' in value or value.startswith("W/") or value == "*":
                raise ValueError("if_match must contain one exact strong resource version")
            headers["If-Match"] = '"' + value + '"'
        if idempotency_key is not None:
            key = _header(idempotency_key, "idempotency_key")
            if not 8 <= len(key) <= 160 or key != key.strip():
                raise ValueError("idempotency_key must contain 8 to 160 characters without surrounding whitespace")
            headers["Idempotency-Key"] = key
        encoded = None
        if body is not None:
            if content_type:
                headers["Content-Type"] = content_type
            encoded = (urllib.parse.urlencode(cast(Mapping[str, object], body)).encode("ascii")
                       if content_type == "application/x-www-form-urlencoded"
                       else json.dumps(body, separators=(",", ":"), sort_keys=True, allow_nan=False).encode("utf-8"))
        return self._send(urllib.request.Request(url, data=encoded, headers=headers, method=method))

    def _send(self, request: urllib.request.Request) -> object:
        try:
            with urllib.request.build_opener(_NoRedirect()).open(request, timeout=self.timeout_seconds) as response:
                if self.on_response is not None:
                    self.on_response(response.status, dict(response.headers.items()))
                body = response.read()
                if response.status == 204:
                    return None
                content_type = response.headers.get("Content-Type", "").lower()
                if "json" in content_type:
                    try:
                        return json.loads(body)
                    except (ValueError, UnicodeError) as error:
                        raise LiquidityOsResponseError("API returned invalid JSON") from error
                if request.get_header("Accept") == "application/json":
                    raise LiquidityOsResponseError("API returned a non-JSON response")
                return body
        except urllib.error.HTTPError as error:
            with error:
                try:
                    payload = json.loads(error.read())
                except (http.client.HTTPException, TimeoutError, OSError) as read_error:
                    raise LiquidityOsTransportError("API response could not be read completely; mutation completion may be unknown") from read_error
                except (ValueError, UnicodeError):
                    payload = None
                detail = payload.get("error") if isinstance(payload, dict) else None
                code = detail if isinstance(detail, str) else detail.get("code") if isinstance(detail, dict) else None
                message = detail.get("message") if isinstance(detail, dict) else None
                correlation_id = detail.get("correlationId") if isinstance(detail, dict) else None
                retryable = detail.get("retryable") if isinstance(detail, dict) else None
                remediation = detail.get("remediation") if isinstance(detail, dict) else None
                field_errors = detail.get("fieldErrors") if isinstance(detail, dict) else None
                raise LiquidityOsApiError(
                    error.code,
                    code if isinstance(code, str) and code else "LIQUIDITY_OS_REQUEST_FAILED",
                    message if isinstance(message, str) and message else f"HTTP {error.code}",
                    correlation_id if isinstance(correlation_id, str) else None,
                    retry_after=error.headers.get("Retry-After"),
                    retryable=retryable if isinstance(retryable, bool) else None,
                    remediation=remediation if isinstance(remediation, str) else None,
                    field_errors=field_errors if isinstance(field_errors, dict) else None,
                ) from error
        except (urllib.error.URLError, http.client.HTTPException, TimeoutError, OSError) as error:
            raise LiquidityOsTransportError("API connection failed, timed out, or returned an incomplete response; mutation completion may be unknown") from error
