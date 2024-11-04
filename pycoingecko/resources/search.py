from typing import cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class Search:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def search(self, query: str) -> dict:
        "Search for coins, categories and markets listed on CoinGecko."
        params = {"query": query}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=CoinGeckoApiUrls.SEARCH, **request)

        return cast(dict, response)
