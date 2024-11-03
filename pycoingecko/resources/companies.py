from typing import cast

from pycoingecko.utils import CoinGeckoApiUrls, IHttp


class Companies:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def holdings(self, *, coin_id: str) -> dict:
        "Query public companies’ bitcoin or ethereum holdings."
        path = CoinGeckoApiUrls.COMPANIES.format(coin_id=coin_id)
        response = self.http.send(path=path)

        return cast(dict, response)
