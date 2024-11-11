from typing import Any, Optional, cast

from pycoingecko.utils import (
    CoinGeckoApiUrls,
    CoinGeckoRequestParams,
    IHttp,
    as_gecko_args,
)


class Coins:
    """CoinGecko Coins API."""

    def __init__(self, http: IHttp) -> None:
        self.http = http

    @as_gecko_args
    def list_all(self, *, include_platform: Optional[bool] = None) -> list:
        """Query all the supported coins on CoinGecko with coins id, name and symbol.

        :param include_platform:    Set to true to include platform contract addresses.
        """
        request: CoinGeckoRequestParams = {}

        if include_platform:
            params = {"include_platform": include_platform}
            request = {"params": params}

        response = self.http.send(path=CoinGeckoApiUrls.COINS_LIST, **request)

        return cast(list, response)

    @as_gecko_args
    def list_with_markets(self, *, vs_currency: str, **kwargs: Any) -> list:
        """Query all the supported coins with price, market cap, volume and market related data.

        :param vs_currency:             Target currency of coins and market data
        :param ids:                     Coins' ids, comma-separated if querying more than 1 coin.
        :param category:                Filter by coin category
        :param order:                   Order results by field
        :param per_page:                Total results per page
        :param page:                    Page through results
        :param sparkline:               Include sparkline 7 days data
        :param price_change_percentage: Include price change percentage timeframe, comma-separated if query more than 1 price change percentage timeframe
        :param locale:                  Language background
        :param precision:               Decimal place for currency price value
        """
        params = {"vs_currency": vs_currency, **kwargs}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=CoinGeckoApiUrls.COINS_MARKETS, **request)

        return cast(list, response)

    @as_gecko_args
    def data_by_id(self, *, coin_id: str, **kwargs: Any) -> dict:
        """Query all the coin data of a coin (name, price, market .... including exchange tickers) on CoinGecko coin page based on a particular coin id

        :param coin_id:                 The coin id
        :param localization:            Set to false to exclude localized languages in response
        :param tickers:                 Include tickers data
        :param market_data:             Include market data
        :param community_data:          Include community data
        :param developer_data:          Include developer data
        :param sparkline:               Include sparkline 7 days data
        """
        path = CoinGeckoApiUrls.COIN.format(id=coin_id)
        request: CoinGeckoRequestParams = {}

        if kwargs:
            request = {"params": kwargs}

        response = self.http.send(path=path, **request)

        return cast(dict, response)

    @as_gecko_args
    def tickers_by_id(self, *, coin_id: str, **kwargs: Any) -> dict:
        """Query the coin tickers on both centralized exchange (cex) and decentralized exchange (dex) based on a particular coin id.

        :param coin_id:                 The coin id
        :param exchange_ids:            Filter tickers by exchange ids, comma-separated if querying more than 1 exchange
        :param include_exchange_logo:   Flag to include exchange's logo
        :param page:                    Page through results
        :param order:                   Order results by field
        :param depth:                   Order book depth
        """
        path = CoinGeckoApiUrls.COIN_TICKERS.format(id=coin_id)
        request: CoinGeckoRequestParams = {}

        if kwargs:
            request = {"params": kwargs}

        response = self.http.send(path=path, **request)

        return cast(dict, response)

    @as_gecko_args
    def historical_data_by_id(
        self, *, coin_id: str, snapshot_date: str, localization: Optional[bool] = None
    ) -> dict:
        """Query the historical data (price, market cap, 24hrs volume, etc) at a given date for a coin based on a particular coin id.

        :param coin_id:                 The coin id
        :param snapshot_date:           The date of snapshot in dd-mm-yyyy
        :param localization:            Set to false to exclude localized languages in response
        """
        request: CoinGeckoRequestParams = {}
        path = CoinGeckoApiUrls.COIN_HISTORY.format(id=coin_id)
        params: dict[str, Any] = {"date": snapshot_date}

        if localization:
            params["localization"] = localization

        request = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def historical_chart_data_by_id(
        self, *, coin_id: str, vs_currency: str, days: str = "1", **kwargs: Any
    ) -> dict:
        """Query the historical price, market cap, volume, and total supply at a given date for a coin in a particular currency based on a particular coin id.

        :param coin_id:                 The coin id
        :param vs_currency:             The target currency of coins
        :param days:                    Data up to number of days ago
        :param interval:                Data interval, leave empty for auto granularity Possible value
        :param percision:               Decimal place for currency price value
        """
        path = CoinGeckoApiUrls.COIN_HISTORY_CHART.format(id=coin_id)
        params = {"vs_currency": vs_currency, "days": days, **kwargs}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def historical_chart_data_within_time_range_by_id(
        self,
        *,
        coin_id: str,
        vs_currency: str,
        from_timestamp: int,
        to_timestamp: int,
        precision: Optional[str] = None,
    ) -> dict:
        """Get the historical chart data of a coin within certain time range in UNIX along with price, market cap and 24hrs volume based on particular coin id.

        :param coin_id:                 The coin id
        :param vs_currency:             The target currency of coins
        :param from_timestamp:          Starting date in UNIX timestamp
        :param to_timestamp:            Ending date in UNIX timestamp
        :param precision:               Decimal place for currency price value
        """
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

    def ohlc_chart_by_id(
        self,
        *,
        coin_id: str,
        vs_currency: str = "usd",
        days: str = "1",
        interval: Optional[str] = None,
        precision: Optional[str] = None,
    ) -> list:
        """Get the OHLC chart (Open, High, Low, Close) of a coin based on particular coin id.

        :param coin_id:                 The coin id
        :param vs_currency:             The target currency of coins
        :param days:                    Data up to number of days ago
        :param interval:                Data interval, leave empty for auto granularity Possible value
        """
        params = {"vs_currency": vs_currency, "days": days}
        path = CoinGeckoApiUrls.COIN_OHLC.format(id=coin_id)

        if interval:
            params["interval"] = interval

        if precision:
            params["precision"] = precision

        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(list, response)
