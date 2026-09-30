# Releasing the Python SDK

The package version is `2.1.0`; the API contract remains `2.0.0`. This release adds typed read-only partner preparation receipt recovery. The repository release workflow builds a wheel and source archive and attaches them to a GitHub release. It does not publish to PyPI.

1. Confirm the proprietary license in `LICENSE.txt` and package metadata. Obtain authorization for any public package publication; public source review does not grant usage or redistribution rights.
2. Regenerate `client.py` from the canonical v2 contract in the main Klineo repository, export the SDK, and review request/response changes. Keep `runtime.py` transport behavior covered by tests.
3. Update the version in `pyproject.toml` and `klineo_liquidity_os/__init__.py`, and add the release notes to `CHANGELOG.md`.
4. In a clean virtual environment, run `python -m pip install build`, `python -m unittest discover -s tests -v`, and `python -m build`. Install the resulting wheel into a second clean environment and confirm the imports and version.
5. Push a reviewed `v2.1.0` tag. The release workflow rejects a tag that differs from the package version. Review the generated wheel and source archive on the release.

For PyPI publication, configure a project-scoped trusted publisher or an appropriate protected release process. Publication is an explicit follow-up and is not performed by this workflow. Never put registry credentials or API tokens in the repository.
