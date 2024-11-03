from typing import Any, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class Exchanges:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def exchanges_list(self, *, per_page: int = 100, page: int = 1) -> list:
        "Query all the supported exchanges with exchanges’ data (id, name, country, .... etc) that have active trading volumes on CoinGecko."
        params = {"per_page": per_page, "page": page}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=CoinGeckoApiUrls.EXCHANGES, **request)

        return cast(list, response)

    def exchanges_list_id_map(self) -> list:
        "Query all the supported coins with price, market cap, volume and market related data."
        response = self.http.send(path=CoinGeckoApiUrls.EXCHANGES_LIST)

        return cast(list, response)

    def exchange_by_id(self, *, exchange_id: str) -> dict:
        "Query all the coin data of a coin (name, price, market .... including exchange tickers) on CoinGecko coin page based on a particular coin id."
        path = CoinGeckoApiUrls.EXCHANGE.format(id=exchange_id)
        response = self.http.send(path=path)

        return cast(dict, response)

    def exchange_tickers_by_id(self, *, exchange_id: str, **kwargs: Any) -> dict:
        "Query exchange's tickers based on exchange’s id."
        path = CoinGeckoApiUrls.EXCHANGE_TICKERS.format(id=exchange_id)
        request: CoinGeckoRequestParams = {}

        if kwargs:
            request = {"params": kwargs}

        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def exchange_volume_chart_by_id(self, *, exchange_id: str, days: int = 1) -> dict:
        "Query the historical volume chart data with time in UNIX and trading volume data in BTC based on exchange’s id."
        path = CoinGeckoApiUrls.EXCHANGE_VOLUME_CHART.format(id=exchange_id)
        params = {"days": days}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)
