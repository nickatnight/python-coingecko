from typing import Optional, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class PoolsOnChain:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def trending_list(self, *, include: str, page: Optional[int] = 1) -> dict:
        "Query all the trending pools across all networks on GeckoTerminal."
        params = {"include": include, "page": page}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(
            path=CoinGeckoApiUrls.ONCHAIN_TRENDING_POOLS, **request
        )

        return cast(dict, response)

    def trending_list_by_network(
        self, *, network: str, include: Optional[str] = None, page: Optional[int] = 1
    ) -> dict:
        "Query the trending pools based on the provided network"
        path = CoinGeckoApiUrls.ONCHAIN_POOLS_TRENDING_BY_NETWORK.format(
            network=network
        )
        params = {"page": page}

        if include:
            params["include"] = include  # type: ignore

        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def data_by_pool_address(
        self, *, network: str, pool_address: str, include: Optional[str] = None
    ) -> dict:
        "Query the specific pool based on the provided network and pool address."
        path = CoinGeckoApiUrls.ONCHAIN_POOL_BY_ADDRESS.format(
            network=network, address=pool_address
        )
        request: CoinGeckoRequestParams = {}

        if include:
            params = {"include": include}
            request = {"params": params}

        response = self.http.send(path=path, **request)

        return cast(dict, response)
