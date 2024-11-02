from typing import cast

from pycoingecko.utils import CoinGeckoApiUrls, IHttp


class Trending:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def trending(self) -> dict:
        "Query trending search coins, nfts and categories on CoinGecko in the last 24 hours."
        response = self.http.send(path=CoinGeckoApiUrls.TRENDING)

        return cast(dict, response)
