from typing import Any, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class Simple:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def coin_price_by_id(self, *, ids: str, vs_currencies: str, **kwargs: Any) -> dict:
        "Query the prices of one or more coins by using their unique Coin API IDs"
        params = {"ids": ids, "vs_currencies": vs_currencies, **kwargs}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=CoinGeckoApiUrls.PRICE, **request)

        return cast(dict, response)

    def coin_price_by_token(
        self,
        *,
        asset_id: str,
        contract_addresses: str,
        vs_currencies: str,
        **kwargs: Any,
    ) -> dict:
        "Query a token price by using token contract address."
        path = CoinGeckoApiUrls.TOKEN_PRICE.format(id=asset_id)
        params = {
            "contract_addresses": contract_addresses,
            "vs_currencies": vs_currencies,
            **kwargs,
        }
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def supported_vs_currencies(self) -> list:
        "Query all the supported currencies on CoinGecko."
        response = self.http.send(path=CoinGeckoApiUrls.SUPPORTED_CURRENCIES)

        return cast(list, response)
