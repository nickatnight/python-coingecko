from typing import Optional, cast

from pycoingecko.resources.global_data import GlobalData
from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams


class GlobalDataPro(GlobalData):
    def volume_chart_within_time_range(
        self, *, days: str, vs_currency: Optional[str] = "usd"
    ) -> dict:
        """query the historical volume chart data in BTC by specifying date range in UNIX based on exchange’s id"""
        params = {"days": days, "vs_currency": vs_currency}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(
            path=CoinGeckoApiUrls.GLOBAL_MARKET_CAP_CHART, **request
        )

        return cast(dict, response)
