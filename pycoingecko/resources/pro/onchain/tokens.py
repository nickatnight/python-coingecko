from typing import Any, Optional, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class TokensOnChain:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def top_pools_by_token_address(
        self,
        *,
        network: str,
        token_address: str,
        **kwargs: Any,
    ) -> dict:
        "Query top pools based on the provided token contract address on a network."
        path = CoinGeckoApiUrls.ONCHAIN_TOKENS_TOP_POOLS.format(
            network=network, token_address=token_address
        )
        request: CoinGeckoRequestParams = {}

        if kwargs:
            request = {"params": kwargs}

        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def data_by_token_address(
        self, *, network: str, address: str, include: Optional[str] = None
    ) -> dict:
        "Query specific token data based on the provided token contract address on a network."
        path = CoinGeckoApiUrls.ONCHAIN_TOKEN_BY_ADDRESS.format(
            network=network, address=address
        )
        request: CoinGeckoRequestParams = {}

        if include:
            params = {"include": include}
            request = {"params": params}

        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def data_by_token_multi_addresses(
        self, *, network: str, addresses: str, include: Optional[str] = None
    ) -> dict:
        "Query multiple tokens data based on the provided token contract addresses on a network"
        path = CoinGeckoApiUrls.ONCHAIN_TOKEN_BY_MULTI_ADDRESSES.format(
            network=network, addresses=addresses
        )
        request: CoinGeckoRequestParams = {}

        if include:
            params = {"include": include}
            request = {"params": params}

        request = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def info_by_token_address(self, *, network: str, address: str) -> dict:
        "Query specific token info such as name,symbol, coingecko id etc. based on provided token contract address on a network."
        path = CoinGeckoApiUrls.ONCHAIN_TOKEN_INFO_BY_ADDRESS.format(
            network=network, address=address
        )
        response = self.http.send(path=path)

        return cast(dict, response)

    def pool_tokens_info_by_pool_address(
        self, *, network: str, pool_address: str
    ) -> dict:
        "Query pool info including base and quote token info based on provided pool contract address on a network."
        path = CoinGeckoApiUrls.ONCHAIN_TOKEN_POOL_INFO_BY_ADDRESS.format(
            network=network, pool_address=pool_address
        )
        response = self.http.send(path=path)

        return cast(dict, response)

    def most_recently_updated(
        self, *, include: Optional[str] = None, network: Optional[str] = None
    ) -> dict:
        "Query 100 most recently updated tokens info of a specific network or across all networks on GeckoTerminal."
        path = CoinGeckoApiUrls.ONCHAIN_TOKEN_MOST_RECENTLY_UPDATED
        params = {}

        if include:
            params["include"] = include

        if network:
            params["network"] = network

        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)
