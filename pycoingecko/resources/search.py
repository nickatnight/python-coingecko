from typing import cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class Search:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def query(self, q: str) -> dict:
        """Search for coins, categories and markets listed on CoinGecko.

        :param q:     Search query phrase
        """
        params = {"query": q}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=CoinGeckoApiUrls.SEARCH, **request)

        return cast(dict, response)
