# Klineo Python SDK

Typed Python client for the Klineo Liquidity Operating System v2 API. Python 3.11 or newer is required. The SDK uses the Python standard library and has no runtime dependencies.

SDK version: `2.1.0`. API contract version: `2.0.0`.

Repository: [Klineo-Ecosystem/klineo-python-sdk](https://github.com/Klineo-Ecosystem/klineo-python-sdk). Developer documentation: [docs.klineo.io](https://docs.klineo.io).

## Install from source

```sh
git clone --branch v2.1.0 https://github.com/Klineo-Ecosystem/klineo-python-sdk.git
cd klineo-python-sdk
python3 -m venv .venv
. .venv/bin/activate
python -m pip install .
```

Use a release tag or reviewed commit when pinning a production installation. PyPI publication is a separate release step; the distribution name is `klineo-liquidity-os` and the import name is `klineo_liquidity_os`.

SDK 2.1.0 adds `get_partner_preparation_receipt_recovery` with `PartnerPreparationReceipt` and `PartnerPreparationReceiptRecovery` types. The operation requires the initiating actor's authorized interactive session and accepts the partner ID, issuer organization ID and original preparation `idempotency_key`. `ACCEPTED` includes the verified committed receipt; `UNRESOLVED` does not establish that a fresh preparation is safe. Recovery does not submit or retry a preparation.

## Configure the API

Use your deployment's complete v2 API URL, including `/api/liquidity-studio/v2`. The SDK does not choose a production API host for you. Use HTTPS outside local development.

```python
import os
from klineo_liquidity_os import LiquidityOsClient

client = LiquidityOsClient(
    base_url=os.environ["KLINEO_API_BASE_URL"],
    organization_id=os.environ["KLINEO_ORGANIZATION_ID"],
    access_token=os.environ["KLINEO_ACCESS_TOKEN"],
    timeout_seconds=30,
)

page = client.list_scores(query={"limit": 10})
print(page)
```

Organization binding is required for scoped service credentials. Issue an API key or OAuth client through your organization's authorized Developer workspace and keep the secret in a secret manager or environment variable. Public endpoints can be called without an organization or token:

```python
public_client = LiquidityOsClient(base_url=os.environ["KLINEO_API_BASE_URL"])
plans = public_client.list_workspace_plans()
```

## OAuth client credentials

The helper sends `client_secret_basic` credentials and a form-encoded grant request. It returns the token response; it does not store, refresh, or automatically install the token.

```python
oauth = LiquidityOsClient(
    base_url=os.environ["KLINEO_API_BASE_URL"],
    organization_id=os.environ["KLINEO_ORGANIZATION_ID"],
)
token = oauth.oauth_client_credentials(
    os.environ["KLINEO_CLIENT_ID"],
    os.environ["KLINEO_CLIENT_SECRET"],
    scopes=("scores:read",),
)
authenticated = LiquidityOsClient(
    base_url=oauth.base_url,
    organization_id=oauth.organization_id,
    access_token=token["access_token"],
)
```

Requested scopes must be a subset of the credential's granted scopes. Credential issuance and rotation return a secret once; repeating a request cannot retrieve it. Service credentials can read or prepare within their exact scopes. The complete client also describes operations reserved for interactive sessions; exposing a method does not grant service access to it. Authority changes require the application's interactive issuer flow.

## Types and operation methods

Every v2 OpenAPI operation has a snake_case method on `LiquidityOsClient`. Request and result `TypedDict` definitions live in `klineo_liquidity_os.client` and the installed package includes a `py.typed` marker. Types describe API payloads; server-side validation remains authoritative.

```python
from klineo_liquidity_os.client import ListScoresQuery

query: ListScoresQuery = {"limit": 10}
scores = client.list_scores(query=query)
```

IDs are supplied as `path` dictionaries and list filters as `query` dictionaries. String path segments and query values are encoded. `None` query values are omitted. Collection methods return the server's pagination envelope; pass `response["meta"]["nextCursor"]` as the next request's `cursor`, and stop when no cursor is returned.

## Writes, versions, and idempotency

Mutation methods require an explicit idempotency key where the API contract requires one. Keep the same 8–160 character key when retrying the same logical mutation with the same body. Generate a different key for a different operation. Revision methods also require the exact current `resourceVersion` as `if_match`; the SDK sends a quoted strong `If-Match` header.

```python
from uuid import uuid4

# sandbox-study.json must contain a validated RunNonCustodialSandboxStudyBody.
import json
with open("sandbox-study.json", encoding="utf-8") as source:
    body = json.load(source)

study = client.run_non_custodial_sandbox_study(
    body=body,
    idempotency_key=str(uuid4()),
)
```

The SDK makes one request per method call and does not automatically retry. After a timeout or lost response, a mutation may already have completed. Reconcile the resource or retry with the original idempotency key. After a version conflict, fetch the current resource and reassess the intended change before submitting it.

Atomic token and quote amounts are decimal strings, including values larger than floating-point precision. Pass and retain them as strings. Pips are integer units defined by the API. The SDK does not convert amounts, sign transactions, hold Safe keys, or bypass simulation, review, policy, timelock, or onchain controls.

## Errors and downloads

```python
from klineo_liquidity_os import (
    LiquidityOsApiError,
    LiquidityOsResponseError,
    LiquidityOsTransportError,
)

try:
    scores = client.list_scores(query={"limit": 10})
except LiquidityOsApiError as error:
    # Keep correlation_id for support. Avoid logging credentials or request bodies.
    print(error.status, error.code, error.correlation_id, error.retry_after)
except LiquidityOsTransportError:
    print("Connection failed or timed out; reconcile any pending mutation.")
except LiquidityOsResponseError:
    print("The successful API response was not valid expected JSON.")
```

HTTP errors expose `status`, `code`, `correlation_id`, `retryable`, `remediation`, `field_errors`, and the raw `Retry-After` value (or `None`). OAuth errors such as `invalid_client` retain their code. Non-JSON or malformed HTTP error bodies still produce `LiquidityOsApiError`. Input boundary errors raise `ValueError` before a request. Redirects are rejected to avoid forwarding credentials or tenant headers.

JSON responses become Python dictionaries or lists. Successful non-JSON download responses become `bytes`; write them using binary mode. A successful HTTP 204 returns `None`.

```python
pdf = public_client.download_public_liquidity_passport(
    path={"slug": "your-public-passport-slug", "format": "pdf"},
)
with open("passport.pdf", "wb") as output:
    output.write(pdf)
```

For verification workflows, set `on_response` to a callback accepting the HTTP status and a copy of the successful response headers. It runs before the body is read, preserving artifact-hash and signature headers alongside a binary download. Header names may vary in casing; normalize them before lookup. The callback does not verify signatures for you.

```python
download_headers = {}
verified_client = LiquidityOsClient(
    base_url=os.environ["KLINEO_API_BASE_URL"],
    on_response=lambda status, headers: download_headers.update(
        {name.lower(): value for name, value in headers.items()}
    ),
)
pdf = verified_client.download_public_liquidity_passport(
    path={"slug": "your-public-passport-slug", "format": "pdf"},
)
# Verify the bytes and captured headers against the issuer's verification bundle.
```

## Develop and release

```sh
python -m unittest discover -s tests -v
python -m pip wheel --no-deps --wheel-dir dist .
```

See [RELEASE.md](RELEASE.md) for verification, versioning, and release artifacts. `client.py` is generated from the canonical v2 OpenAPI contract in the main Klineo repository; `runtime.py` is the maintained transport. Regenerate in that source repository, validate the SDK, and export the result. Do not hand edit generated operation signatures.

The SDK is proprietary and all rights are reserved. Public source is available for review; obtain written permission before using, modifying, or redistributing it. See [LICENSE.txt](LICENSE.txt).
