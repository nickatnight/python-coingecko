from pycoingecko.clients.demo import CoinGeckoDemoClient
from pycoingecko.clients.pro import CoinGeckoProClient
from pycoingecko.utils import (
    DEMO_COIN_GECKO_API_URL,
    PRO_COIN_GECKO_API_URL,
    RequestsClient,
)
from pycoingecko.utils.exceptions import CoinGeckoClientError
from pycoingecko.utils.helpers import get_client_api_methods


class CoinGecko:
    """Main CoinGecko API Client

    :param api_key:         CoinGecko API key
    :param is_pro:          Flag to indicate which client to use (Demo or Pro)
    :param use_onchain:     Flag to indicate if client should support onchain api (Pro only)
    """

    def __init__(
        self, api_key: str = "", is_pro: bool = False, use_onchain: bool = False
    ) -> None:
        if not is_pro and use_onchain:
            raise CoinGeckoClientError("Onchain data is only available for pro API")

        header_name = "x-cg-pro-api-key" if is_pro else "x-cg-demo-api-key"
        url = PRO_COIN_GECKO_API_URL if is_pro else DEMO_COIN_GECKO_API_URL
        http = RequestsClient(base_url=url, headers={header_name: api_key})
        client = CoinGeckoProClient if is_pro else CoinGeckoDemoClient

        attr_list = get_client_api_methods(client=client)

        for attr in attr_list:
            setattr(self, attr, getattr(client(http), attr))
