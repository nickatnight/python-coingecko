from typing import cast

from pycoingecko.utils import CoinGeckoApiUrls, IHttp


class ExchangeRates:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def btc_to_currency(self) -> dict:
        "Query BTC exchange rates with other currencies."
        response = self.http.send(path=CoinGeckoApiUrls.BTC_TO_CURRENCY)

        return cast(dict, response)
