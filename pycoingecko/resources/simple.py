from typing import Any, cast

from pycoingecko.utils import (
    CoinGeckoApiUrls,
    CoinGeckoRequestParams,
    IHttp,
    as_gecko_args,
)


class Simple:
    """CionGecko Simple API."""

    def __init__(self, http: IHttp) -> None:
        self.http = http

    @as_gecko_args
    def price_by_id(self, *, ids: str, vs_currencies: str, **kwargs: Any) -> dict:
        """Query the prices of one or more coins by using their unique Coin API IDs

        :param ids:                Coins' ids, comma-separated if querying more than 1 coin.
        :param vs_currencies:      Target currency of coins, comma-separated if querying more than 1 currency.
        """
        params = {"ids": ids, "vs_currencies": vs_currencies, **kwargs}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=CoinGeckoApiUrls.PRICE, **request)

        return cast(dict, response)

    @as_gecko_args
    def price_by_token_addresses(
        self,
        *,
        asset_id: str,
        contract_addresses: str,
        vs_currencies: str,
        **kwargs: Any,
    ) -> dict:
        """Query a token price by using token contract address.

        :param asset_id:           Asset platform's id
        :param contract_addresses: The contract address of a token
        :param vs_currencies:      Target currency of coins, comma-separated if querying more than 1 currency.
        """
        path = CoinGeckoApiUrls.TOKEN_PRICE.format(id=asset_id)
        params = {
            "contract_addresses": contract_addresses,
            "vs_currencies": vs_currencies,
            **kwargs,
        }
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def supported_currencies(self) -> list:
        """Query all the supported currencies on CoinGecko."""
        response = self.http.send(path=CoinGeckoApiUrls.SUPPORTED_CURRENCIES)

        return cast(list, response)
