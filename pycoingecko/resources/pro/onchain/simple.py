from typing import cast

from pycoingecko.utils import CoinGeckoApiUrls, IHttp


class SimpleOnChain:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def token_price_by_address(self, *, network: str, addresses: str) -> dict:
        "Get token price based on the provided token contract address on a network."
        path = CoinGeckoApiUrls.ONCHAIN_TOKEN_PRICE_BY_ADDRESS.format(
            network=network, addresses=addresses
        )
        response = self.http.send(path=path)

        return cast(dict, response)
