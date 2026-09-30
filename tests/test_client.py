import base64
import http.client
import io
import json
import unittest
import urllib.error
import urllib.parse
from email.message import Message
from unittest.mock import patch

from klineo_liquidity_os import (
    LiquidityOsApiError,
    LiquidityOsClient,
    LiquidityOsResponseError,
    LiquidityOsTransportError,
)


class Response:
    def __init__(self, body=b'{"data":[],"meta":{"count":0,"hasMore":false}}', content_type="application/json", status=200):
        self.body = body
        self.status = status
        self.headers = {"Content-Type": content_type}

    def read(self):
        return self.body

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


class ClientTests(unittest.TestCase):
    def setUp(self):
        self.client = LiquidityOsClient("https://api.example.test/api/liquidity-studio/v2/", "org-1", "secret-token", 7)
        self.patch = patch("urllib.request.build_opener")
        self.opener = self.patch.start().return_value
        self.addCleanup(self.patch.stop)
        self.opener.open.return_value = Response()

    def request(self):
        self.assertEqual(self.opener.open.call_count, 1, "Each method makes exactly one HTTP attempt")
        request = self.opener.open.call_args.args[0]
        self.assertEqual(self.opener.open.call_args.kwargs["timeout"], 7)
        return request

    def test_list_request_preserves_tenant_auth_and_query(self):
        result = self.client.list_scores(query={"limit": 10, "cursor": "opaque/+?="})
        request = self.request()
        self.assertEqual(request.method, "GET")
        self.assertEqual(urllib.parse.urlsplit(request.full_url).path, "/api/liquidity-studio/v2/scores")
        self.assertEqual(urllib.parse.parse_qs(urllib.parse.urlsplit(request.full_url).query), {"limit": ["10"], "cursor": ["opaque/+?="]})
        self.assertEqual(request.get_header("Authorization"), "Bearer secret-token")
        self.assertEqual(request.get_header("X-klineo-organization-id"), "org-1")
        self.assertEqual(result["meta"]["hasMore"], False)

    def test_path_segments_are_encoded(self):
        self.client.get_scores(path={"id": "record/with?reserved#parts"})
        self.assertIn("record%2Fwith%3Freserved%23parts", self.request().full_url)

    def test_mutation_uses_exact_version_and_idempotency_without_amount_conversion(self):
        amount = "900719925474099300000000000001"
        self.client.supersede_intents(path={"id": "intent-1"}, body={"payload": {"capitalCeilingQuote": amount}}, if_match="resource-v1", idempotency_key="same-logical-request")
        request = self.request()
        self.assertEqual(request.get_header("If-match"), '"resource-v1"')
        self.assertEqual(request.get_header("Idempotency-key"), "same-logical-request")
        self.assertEqual(json.loads(request.data)["payload"]["capitalCeilingQuote"], amount)
        self.assertEqual(request.get_header("Content-type"), "application/json")

    def test_quoted_version_is_not_double_quoted(self):
        self.client.supersede_intents(path={"id": "intent-1"}, body={}, if_match='"resource-v1"', idempotency_key="request-1")
        self.assertEqual(self.request().get_header("If-match"), '"resource-v1"')

    def test_oauth_basic_credentials_use_form_encoding(self):
        self.opener.open.return_value = Response(b'{"access_token":"returned-token","token_type":"Bearer","expires_in":3600}')
        result = self.client.oauth_client_credentials("id:/ +", "secret:/ +", ("scores:read", "proof:read"))
        request = self.request()
        encoded = request.get_header("Authorization").split(" ", 1)[1]
        client_id, secret = base64.b64decode(encoded).decode().split(":", 1)
        self.assertEqual(urllib.parse.unquote_plus(client_id), "id:/ +")
        self.assertEqual(urllib.parse.unquote_plus(secret), "secret:/ +")
        self.assertEqual(urllib.parse.parse_qs(request.data.decode()), {"grant_type": ["client_credentials"], "scope": ["scores:read proof:read"]})
        self.assertEqual(result["access_token"], "returned-token")
        self.assertEqual(self.client.access_token, "secret-token", "OAuth helper does not install tokens")

    def http_error(self, payload, status=429):
        headers = Message()
        headers["Retry-After"] = "12"
        self.opener.open.side_effect = urllib.error.HTTPError("https://api.example.test", status, "error", headers, io.BytesIO(payload))

    def test_structured_api_error_preserves_support_and_retry_details(self):
        self.http_error(json.dumps({"error": {"code": "RATE_LIMITED", "message": "Wait", "correlationId": "request-123", "retryable": True, "remediation": "Retry later", "fieldErrors": {"limit": ["too high"]}}}).encode())
        with self.assertRaises(LiquidityOsApiError) as caught:
            self.client.list_scores()
        error = caught.exception
        self.assertEqual((error.status, error.code, str(error), error.correlation_id, error.retry_after), (429, "RATE_LIMITED", "Wait", "request-123", "12"))
        self.assertEqual((error.retryable, error.remediation, error.field_errors), (True, "Retry later", {"limit": ["too high"]}))
        self.request()

    def test_oauth_string_error_preserves_code(self):
        self.http_error(b'{"error":"invalid_client"}', status=401)
        with self.assertRaises(LiquidityOsApiError) as caught:
            self.client.oauth_client_credentials("id", "secret")
        self.assertEqual((caught.exception.status, caught.exception.code), (401, "invalid_client"))

    def test_malformed_http_errors_remain_api_errors(self):
        for payload in (b"<html>proxy</html>", b"null", b"[]", b'{"error":null}', b'{"error":{"code":3,"message":{},"correlationId":false}}'):
            with self.subTest(payload=payload):
                self.http_error(payload, status=503)
                with self.assertRaises(LiquidityOsApiError) as caught:
                    self.client.list_scores()
                self.assertEqual((caught.exception.status, caught.exception.code, str(caught.exception)), (503, "LIQUIDITY_OS_REQUEST_FAILED", "HTTP 503"))

    def test_network_failure_is_not_retried(self):
        self.opener.open.side_effect = urllib.error.URLError("connection refused")
        with self.assertRaises(LiquidityOsTransportError):
            self.client.list_scores()
        self.request()

    def test_truncated_success_and_error_responses_are_transport_errors(self):
        class Socket:
            def makefile(self, *args):
                return io.BytesIO(b"HTTP/1.1 " + self.status + b"\r\nContent-Type: application/json\r\nContent-Length: 50\r\n\r\n{}")

        for status in (200, 503):
            with self.subTest(status=status):
                socket = Socket()
                socket.status = str(status).encode() + b" Test"
                response = http.client.HTTPResponse(socket)
                response.begin()
                self.opener.open.reset_mock()
                self.opener.open.side_effect = None
                if status == 200:
                    self.opener.open.return_value = response
                else:
                    self.opener.open.side_effect = urllib.error.HTTPError(
                        self.client.base_url, status, "error", response.headers, response
                    )
                with self.assertRaises(LiquidityOsTransportError) as caught:
                    self.client.list_scores()
                self.assertIsInstance(caught.exception.__cause__, http.client.IncompleteRead)
                self.request()

    def test_invalid_http_status_is_a_transport_error_without_retry(self):
        self.opener.open.side_effect = http.client.BadStatusLine("invalid status")
        with self.assertRaises(LiquidityOsTransportError) as caught:
            self.client.list_scores()
        self.assertIsInstance(caught.exception.__cause__, http.client.BadStatusLine)
        self.request()

    def test_invalid_successful_response_has_distinct_error(self):
        for response in (Response(b"not-json"), Response(b"<html>proxy</html>", "text/html")):
            with self.subTest(response=response):
                self.opener.open.return_value = response
                with self.assertRaises(LiquidityOsResponseError):
                    self.client.list_scores()

    def test_binary_download_and_no_content(self):
        self.opener.open.return_value = Response(b"%PDF-test", "application/pdf")
        self.assertEqual(self.client.download_public_liquidity_passport(path={"slug": "published", "format": "pdf"}), b"%PDF-test")
        self.opener.open.return_value = Response(b"", "", 204)
        self.assertIsNone(self.client.list_scores())

    def test_public_client_does_not_send_credentials(self):
        client = LiquidityOsClient(self.client.base_url)
        client.list_workspace_plans()
        request = self.opener.open.call_args.args[0]
        self.assertIsNone(request.get_header("Authorization"))
        self.assertIsNone(request.get_header("X-klineo-organization-id"))

    def test_secret_is_not_in_client_repr(self):
        self.assertNotIn("secret-token", repr(self.client))

    def test_response_observer_captures_signed_download_headers(self):
        observations = []
        client = LiquidityOsClient(self.client.base_url, on_response=lambda status, headers: observations.append((status, headers)))
        response = Response(b"%PDF-test", "application/pdf")
        response.headers["x-klineo-artifact-hash"] = "artifact-hash"
        response.headers["x-klineo-signature"] = "signature"
        self.opener.open.return_value = response
        self.assertEqual(client.download_public_liquidity_passport(path={"slug": "published", "format": "pdf"}), b"%PDF-test")
        self.assertEqual(observations, [(200, {"Content-Type": "application/pdf", "x-klineo-artifact-hash": "artifact-hash", "x-klineo-signature": "signature"})])

    def test_invalid_configuration_fails_before_network(self):
        for url in ("", "/api/v2", "ftp://example.test", "https://user:secret@example.test", "https://example.test?q=x", "https://example.test#part", "https://example.test/?", "https://example.test/\\path", "https://example.test/\npath", "https://example.test:bad"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                LiquidityOsClient(url)
        for timeout in (0, -1, float("nan"), float("inf"), True, "30"):
            with self.subTest(timeout=timeout), self.assertRaises(ValueError):
                LiquidityOsClient(self.client.base_url, timeout_seconds=timeout)
        for argument in ({"organization_id": "org\r\nX-Evil: value"}, {"access_token": "token\n"}, {"access_token": ""}):
            with self.subTest(argument=argument), self.assertRaises(ValueError):
                LiquidityOsClient(self.client.base_url, **argument)
        self.opener.open.assert_not_called()

    def test_invalid_write_headers_paths_and_json_fail_before_network(self):
        for key in ("", "short", " request-1", "request-1\r\n", "x" * 161):
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.client.run_non_custodial_sandbox_study(body={}, idempotency_key=key)
        for version in ("", "*", 'W/"v1"', '""', 'bad"quote', "bad\nversion"):
            with self.subTest(version=version), self.assertRaises(ValueError):
                self.client.supersede_intents(path={"id": "valid"}, body={}, if_match=version, idempotency_key="request-1")
        for path in ({}, {"id": ""}, {"id": ".."}, {"id": True}, {"id": "valid", "extra": "unexpected"}):
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.client.get_scores(path=path)
        with self.assertRaises(ValueError):
            self.client.run_non_custodial_sandbox_study(body={"bad": float("nan")}, idempotency_key="request-1")
        self.opener.open.assert_not_called()


if __name__ == "__main__":
    unittest.main()
