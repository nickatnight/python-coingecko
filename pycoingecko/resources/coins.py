from typing import Any, Optional, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class Coins:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def coins_list(self, *, include_platform: bool = False) -> list:
        "Query all the supported coins on CoinGecko with coins id, name and symbol."
        params = {"include_platform": include_platform}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=CoinGeckoApiUrls.COINS_LIST, **request)

        return cast(list, response)

    def coins_markets(self, *, vs_currency: str, **kwargs: Any) -> list:
        "Query all the supported coins with price, market cap, volume and market related data."
        params = {"vs_currency": vs_currency, **kwargs}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=CoinGeckoApiUrls.COINS_MARKETS, **request)

        return cast(list, response)

    def coin_by_id(self, *, coin_id: str, **kwargs: Any) -> dict:
        "Query all the coin data of a coin (name, price, market .... including exchange tickers) on CoinGecko coin page based on a particular coin id."
        path = CoinGeckoApiUrls.COIN.format(id=coin_id)
        request: CoinGeckoRequestParams = {}

        if kwargs:
            request = {"params": kwargs}

        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def coin_tickers_by_id(self, *, coin_id: str, **kwargs: Any) -> dict:
        "Query the coin tickers on both centralized exchange (cex) and decentralized exchange (dex) based on a particular coin id."
        path = CoinGeckoApiUrls.COIN_TICKERS.format(id=coin_id)
        request: CoinGeckoRequestParams = {}

        if kwargs:
            request = {"params": kwargs}

        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def coin_history_by_id(
        self, *, coin_id: str, snapshot_date: str, localization: bool = True
    ) -> dict:
        "Query the historical data (price, market cap, 24hrs volume, etc) at a given date for a coin based on a particular coin id."
        path = CoinGeckoApiUrls.COIN_HISTORY.format(id=coin_id)
        params = {"date": snapshot_date, "localization": localization}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def coin_history_chart_by_id(
        self, *, coin_id: str, vs_currency: str, days: str = "1", **kwargs: Any
    ) -> dict:
        "Query the historical price, market cap, volume, and total supply at a given date for a coin in a particular currency based on a particular coin id."
        path = CoinGeckoApiUrls.COIN_HISTORY_CHART.format(id=coin_id)
        params = {"vs_currency": vs_currency, "days": days, **kwargs}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def coin_history_chart_range_by_id(
        self,
        *,
        coin_id: str,
        vs_currency: str,
        from_timestamp: int,
        to_timestamp: int,
        precision: Optional[str] = None,
    ) -> dict:
        "Get the historical chart data of a coin within certain time range in UNIX along with price, market cap and 24hrs volume based on particular coin id."
        path = CoinGeckoApiUrls.COIN_HISTORY_TIME_RANGE.format(id=coin_id)
        params = {
            "vs_currency": vs_currency,
            "from": from_timestamp,
            "to": to_timestamp,
        }

        if precision:
            params["precision"] = precision

        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def coin_ohlc_by_id(
        self,
        *,
        coin_id: str,
        vs_currency: str = "usd",
        days: str = "1",
        precision: Optional[str] = None,
    ) -> list:
        "Get the historical OHLC (Open, High, Low, Close) of a coin within a range in UNIX timestamp."
        params = {"vs_currency": vs_currency, "days": days}
        path = CoinGeckoApiUrls.COIN_OHLC.format(id=coin_id)

        if precision:
            params["precision"] = precision

        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(list, response)
