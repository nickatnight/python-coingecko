from typing import cast

from pycoingecko.utils import CoinGeckoApiUrls, IHttp


class GlobalData:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def crypto_market_data(self) -> dict:
        """Query cryptocurrency global data including active cryptocurrencies, markets, total crypto market cap and etc."""
        response = self.http.send(path=CoinGeckoApiUrls.GLOBAL)

        return cast(dict, response)

    def defi_market_data(self) -> dict:
        """Query top 100 cryptocurrency global decentralized finance (defi) data including defi market cap, trading volume."""
        response = self.http.send(path=CoinGeckoApiUrls.GLOBAL_DEFI)

        return cast(dict, response)
