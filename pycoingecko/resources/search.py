from typing import Any, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class Search:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def search(self, **kwargs: Any) -> dict:
        "Search for coins, categories and markets listed on CoinGecko."
        request: CoinGeckoRequestParams = {}

        if kwargs:
            request = {"params": kwargs}

        response = self.http.send(path=CoinGeckoApiUrls.SEARCH, **request)

        return cast(dict, response)
