from typing import Any, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class OHLCVOnChain:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def chart_by_pool_address(
        self, *, network: str, pool_address: str, timeframe: str, **kwargs: Any
    ) -> dict:
        "Get the OHLCV chart (Open, High, Low, Close, Volume) of a pool based on the provided pool address on a network."
        path = CoinGeckoApiUrls.ONCHAIN_OHLCV_BY_POOL_ADDRESS.format(
            network=network, pool_address=pool_address, timeframe=timeframe
        )
        request: CoinGeckoRequestParams = {}

        if kwargs:
            request = {"params": kwargs}

        response = self.http.send(path=path, **request)

        return cast(dict, response)
