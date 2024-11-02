from typing import cast

from pycoingecko.utils import CoinGeckoApiUrls, IHttp


class Ping:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def ping(self) -> dict:
        "Check the API server status"
        response = self.http.send(path=CoinGeckoApiUrls.PING)

        return cast(dict, response)
