"""Read one score page using environment-managed credentials."""
import os
from klineo_liquidity_os import LiquidityOsClient


def main() -> None:
    client = LiquidityOsClient(
        base_url=os.environ["KLINEO_API_BASE_URL"],
        organization_id=os.environ["KLINEO_ORGANIZATION_ID"],
        access_token=os.environ["KLINEO_ACCESS_TOKEN"],
    )
    print(client.list_scores(query={"limit": 10}))


if __name__ == "__main__":
    main()
