from typing import Optional, cast

from pycoingecko.resources.coins import Coins
from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams


class CoinsPro(Coins):
    def top_gainers_and_losers(
        self,
        *,
        vs_currency: str,
        duration: Optional[str] = None,
        top_coins: Optional[str] = None,
    ) -> list:
        "Query the top 30 coins with largest price gain and loss by a specific time duration"
        params = {"vs_currency": vs_currency}

        if duration:
            params["duration"] = duration

        if top_coins:
            params["top_coins"] = top_coins

        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(
            path=CoinGeckoApiUrls.COIN_TOP_GAINERS_AND_LOSERS, **request
        )

        return cast(list, response)

    def recently_added(self) -> list:
        "Query the latest 200 coins that recently listed on CoinGecko"
        response = self.http.send(path=CoinGeckoApiUrls.COIN_RECENTLY_ADDED)

        return cast(list, response)

    def ohlc_chart_within_time_range(
        self,
        *,
        coin_id: str,
        vs_currency: str,
        from_timestamp: int,
        to_timestamp: int,
        interval: str,
    ) -> list:
        "Get the OHLC chart (Open, High, Low, Close) of a coin within a range of timestamp based on particular coin id."
        path = CoinGeckoApiUrls.COIN_OHLC_CHART_TIME_RANGE.format(id=coin_id)
        params = {
            "vs_currency": vs_currency,
            "from": from_timestamp,
            "to": to_timestamp,
            "interval": interval,
        }
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(list, response)

    def circulating_supply(
        self, *, coin_id: str, days: str, interval: Optional[str] = None
    ) -> dict:
        "Query historical circulating supply of a coin by number of days away from now based on provided coin id."
        path = CoinGeckoApiUrls.COIN_CIRCULATING_SUPPLY.format(coin_id=coin_id)
        params = {"days": days}

        if interval:
            params["interval"] = interval

        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def circulating_supply_within_time_range(
        self,
        *,
        coin_id: str,
        from_timestamp: int,
        to_timestamp: int,
    ) -> dict:
        "Query historical circulating supply of a coin within a range of timestamp based on provided coin id."
        path = CoinGeckoApiUrls.COIN_CIRCULATING_SUPPLY_TIME_RANGE.format(id=coin_id)
        params = {
            "from": from_timestamp,
            "to": to_timestamp,
        }
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def total_supply(
        self, *, coin_id: str, days: str, interval: Optional[str] = None
    ) -> dict:
        "Query historical total supply of a coin by number of days away from now based on provided coin id."
        path = CoinGeckoApiUrls.COIN_TOTAL_SUPPLY.format(id=coin_id)
        params = {"days": days}

        if interval:
            params["interval"] = interval

        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def total_supply_within_time_range(
        self,
        *,
        coin_id: str,
        from_timestamp: int,
        to_timestamp: int,
    ) -> dict:
        "Query historical total supply of a coin, within a range of timestamp based on the provided coin id"
        path = CoinGeckoApiUrls.COIN_TOTAL_SUPPLY_TIME_RANGE.format(id=coin_id)
        params = {
            "from": from_timestamp,
            "to": to_timestamp,
        }
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)
