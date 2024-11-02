from typing import Any, Optional, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class Contract:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def coin_data_by_token_address(
        self, *, coin_id: str, contract_address: str
    ) -> dict:
        "Query all the coin data (name, price, market .... including exchange tickers) on CoinGecko coin page based on asset platform and particular token contract address."
        path = CoinGeckoApiUrls.COINS_CONTRACT_ADDRESS.format(
            id=coin_id, contract_address=contract_address
        )
        response = self.http.send(path=path)

        return cast(dict, response)

    def coin_historical_chart_by_token_address(
        self,
        *,
        coin_id: str,
        contract_address: str,
        vs_currency: str,
        days: str = "1",
        **kwargs: Any,
    ) -> dict:
        "Get the historical chart data including time in UNIX, price, market cap and 24hrs volume based on asset platform and particular token contract address."
        path = CoinGeckoApiUrls.COINS_CONTRACT_CHART_ADDRESS_BY_TOKEN.format(
            id=coin_id, contract_address=contract_address
        )
        params = {"vs_currency": vs_currency, "days": days, **kwargs}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def coin_historical_chart_range_by_token_address(
        self,
        *,
        coin_id: str,
        contract_address: str,
        vs_currency: str,
        from_timestamp: int,
        to_timestamp: int,
        precision: Optional[str] = None,
    ) -> dict:
        "Get the historical chart data within certain time range in UNIX along with price, market cap and 24hrs volume based on asset platform and particular token contract address."
        path = CoinGeckoApiUrls.COINS_CONTRACT_CHART_RANGE_ADDRESS_BY_TOKEN.format(
            id=coin_id, contract_address=contract_address
        )
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
