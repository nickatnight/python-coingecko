from typing import Optional, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class Derivatives:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def ticker_list(self) -> list:
        "Query all the tickers from derivatives exchanges on CoinGecko."
        response = self.http.send(path=CoinGeckoApiUrls.DERIVATIVES_TICKERS)

        return cast(list, response)

    def exchanges_list_with_data(
        self,
        *,
        order: str = "open_interest_btc_desc",
        per_page: int = 100,
        page: int = 1,
    ) -> list:
        "Query all the derivatives exchanges with related data (id, name, open interest, .... etc) on CoinGecko."
        params = {"order": order, "per_page": per_page, "page": page}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(
            path=CoinGeckoApiUrls.DERIVATIVES_EXCHANGES, **request
        )

        return cast(list, response)

    def exchange_by_id(
        self, *, exchange_id: str, include_tickers: Optional[str] = None
    ) -> dict:
        "Query the derivatives exchange’s related data (id, name, open interest, .... etc) based on the exchanges’ id."
        path = CoinGeckoApiUrls.DERIVATIVES_EXCHANGE.format(id=exchange_id)
        request: CoinGeckoRequestParams = {}

        if include_tickers:
            params = {"include_tickers": include_tickers}
            request = {"params": params}

        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def exchanges_list_id_map(self) -> list:
        "Query all the derivatives exchanges with id and name on CoinGecko."
        response = self.http.send(path=CoinGeckoApiUrls.DERIVATIVES_EXCHANGE_LIST)

        return cast(list, response)
