from typing import Optional, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class DexesOnChain:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def networks_list(self, *, network: str, page: Optional[int] = 1) -> dict:
        "Query all the supported decentralized exchanges (dexes) based on the provided network on GeckoTerminal."
        path = CoinGeckoApiUrls.ONCHAIN_DEXES_BY_NETWORK.format(network=network)
        request: CoinGeckoRequestParams = {}

        if page:
            params = {"page": page}
            request = {"params": params}

        response = self.http.send(path=path, **request)

        return cast(dict, response)
