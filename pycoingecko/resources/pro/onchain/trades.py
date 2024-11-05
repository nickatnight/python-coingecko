from typing import Optional, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class TradesOnChain:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def past_24_hour_trades_by_pool_address(
        self,
        *,
        network: str,
        pool_address: str,
        trade_volume_in_usd_greater_than: Optional[int] = 0,
    ) -> dict:
        "Query the last 300 trades in the past 24 hours based on the provided pool address"
        path = CoinGeckoApiUrls.ONCHAIN_TRADES_BY_POOL_ADDRESS.format(
            network=network, pool_address=pool_address
        )
        params = {"trade_volume_in_usd_greater_than": trade_volume_in_usd_greater_than}
        request: CoinGeckoRequestParams = {"params": params}

        response = self.http.send(path=path, **request)

        return cast(dict, response)
