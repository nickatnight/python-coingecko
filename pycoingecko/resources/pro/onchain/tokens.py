from typing import Any, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class TokensOnChain:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def top_pools_by_token_address(
        self,
        *,
        network: str,
        token_address: str,
        **kwargs: Any,
    ) -> dict:
        "Query top pools based on the provided token contract address on a network."
        path = CoinGeckoApiUrls.ONCHAIN_TOKENS_TOP_POOLS.format(
            network=network, token_address=token_address
        )
        request: CoinGeckoRequestParams = {}

        if kwargs:
            request = {"params": kwargs}

        response = self.http.send(path=path, **request)

        return cast(dict, response)
