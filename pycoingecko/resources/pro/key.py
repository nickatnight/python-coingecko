from typing import cast

from pycoingecko.utils import CoinGeckoApiUrls, IHttp


class Key:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def key(self) -> dict:
        "Monitor your account's API usage, including rate limits, monthly total credits, remaining credits, and more."
        response = self.http.send(path=CoinGeckoApiUrls.KEY)

        return cast(dict, response)
