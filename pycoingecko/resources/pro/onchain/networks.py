from typing import Optional, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class NetworksOnChain:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def networks_list(self, *, page: Optional[int] = None) -> dict:
        "Query all the supported networks on GeckoTerminal."
        request: CoinGeckoRequestParams = {}

        if page:
            params = {"page": page}
            request = {"params": params}

        response = self.http.send(path=CoinGeckoApiUrls.ONCHAIN_NETWORKS, **request)

        return cast(dict, response)
