from pycoingecko.clients.demo import CoinGeckoDemoClient
from pycoingecko.clients.pro import CoinGeckoProClient
from pycoingecko.utils import (
    DEMO_COIN_GECKO_API_URL,
    PRO_COIN_GECKO_API_URL,
    RequestsClient,
)
from pycoingecko.utils.helpers import get_client_api_methods


__version__ = "0.0.7"


class CoinGecko:
    """Main CoinGecko API Client

    :param api_key:         CoinGecko API key
    :param is_pro:          Flag to indicate which client to use (Demo or Pro)
    """

    def __init__(self, api_key: str, is_pro: bool = False) -> None:
        header_name = "x-cg-demo-api-key"
        url = DEMO_COIN_GECKO_API_URL
        client = CoinGeckoDemoClient

        if is_pro:
            header_name = "x-cg-pro-api-key"
            url = PRO_COIN_GECKO_API_URL
            client = CoinGeckoProClient

        http = RequestsClient(
            base_url=url,
            headers={header_name: api_key, "User-Agent": f"pycoingecko/v{__version__}"},
        )
        attr_list = get_client_api_methods(client=client)

        for attr in attr_list:
            setattr(self, attr, getattr(client(http), attr))
