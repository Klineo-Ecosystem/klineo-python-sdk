"""Download an issuer-disclosed public passport PDF."""
import argparse
import os
from pathlib import Path
from klineo_liquidity_os import LiquidityOsClient


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug")
    parser.add_argument("output", type=Path)
    arguments = parser.parse_args()
    client = LiquidityOsClient(base_url=os.environ["KLINEO_API_BASE_URL"])
    content = client.download_public_liquidity_passport(path={"slug": arguments.slug, "format": "pdf"})
    arguments.output.write_bytes(content)


if __name__ == "__main__":
    main()
