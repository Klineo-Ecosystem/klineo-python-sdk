# Changelog

## 2.0.0

- Typed methods for the complete Liquidity Operating System v2 API contract.
- Standalone Python 3.11+ packaging with no runtime dependencies and a PEP 561 type marker.
- Scoped bearer credentials and OAuth `client_secret_basic`, tenant binding, explicit idempotency, strong version headers, pagination, and binary downloads.
- Validated configuration and request boundaries; redirects rejected; access token omitted from the client representation.
- Structured HTTP, connection, and invalid-response errors, including OAuth error codes and `Retry-After`.
- Unit tests, runnable examples, build CI, and version-tagged release artifacts.
