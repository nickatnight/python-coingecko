from typing import cast

from pycoingecko.resources.exchanges import Exchanges
from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams


class ExchangesPro(Exchanges):
    def volume_chart_within_time_range(
        self, *, exchange_id: str, from_timestamp: int, to_timestamp: int
    ) -> list:
        """query the historical volume chart data in BTC by specifying date range in UNIX based on exchange’s id"""
        path = CoinGeckoApiUrls.EXCHANGE_VOLUME_CHART_TIME_RANGE.format(id=exchange_id)
        params = {"from": from_timestamp, "to": to_timestamp}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(list, response)
