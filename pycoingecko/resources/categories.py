from typing import Optional, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class Categories:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def categories_list(self) -> list:
        "Query all the coins categories on CoinGecko."
        response = self.http.send(path=CoinGeckoApiUrls.CATEGORIES)

        return cast(list, response)

    def categories_list_with_market_data(self, *, order: Optional[str] = None) -> list:
        "Query all the coins categories with market data (market cap, volume, etc.) on CoinGecko."
        request: CoinGeckoRequestParams = {}

        if order:
            params = {"order": order}
            request = {"params": params}

        response = self.http.send(path=CoinGeckoApiUrls.CATEGORIES_MARKETS, **request)

        return cast(list, response)
