from typing import Optional, cast

from pycoingecko.resources.nfts import NFTs
from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams


class NFTsPro(NFTs):
    def collection_with_market_data(
        self,
        *,
        asset_platform_id: Optional[str] = None,
        order: Optional[str] = None,
        per_page: Optional[int] = 100,
        page: Optional[int] = 1,
    ) -> list:
        "Query all the supported NFT collections with floor price, market cap, volume and market related data on CoinGecko."
        params = {}
        request: CoinGeckoRequestParams = {}

        if asset_platform_id:
            params["asset_platform_id"] = asset_platform_id

        if order:
            params["order"] = order

        if per_page:
            params["per_page"] = per_page  # type: ignore

        if page:
            params["page"] = page  # type: ignore

        if params:
            request = {"params": params}

        path = CoinGeckoApiUrls.NFTS_MARKET
        response = self.http.send(path=path, **request)

        return cast(list, response)

    def market_chart_by_id(self, *, nft_id: str, days: str) -> dict:
        "Query historical market data of a NFT collection, including floor price, market cap, and 24h volume, by number of days away from now."
        path = CoinGeckoApiUrls.NFTS_HISTORICAL_CHART.format(id=nft_id)
        params = {"days": days}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def historical_chart_by_contract_address(
        self, *, asset_platform_id: str, contract_address: str, days: str
    ) -> dict:
        "Query historical market data of a NFT collection, including floor price, market cap, and 24h volume, by number of days away from now based on the provided contract address"
        path = CoinGeckoApiUrls.NFTS_HISTORICAL_CHART_BY_ADDRESS.format(
            asset_platform_id=asset_platform_id, contract_address=contract_address
        )
        params = {"days": days}
        request: CoinGeckoRequestParams = {"params": params}
        response = self.http.send(path=path, **request)

        return cast(dict, response)

    def tickers_by_id(self, *, nft_id: str) -> dict:
        "Query the latest floor price and 24h volume of a NFT collection, on each NFT marketplace, e.g. OpenSea and LooksRare"
        path = CoinGeckoApiUrls.NFTS_TICKERS_BY_ID.format(id=nft_id)
        response = self.http.send(path=path)

        return cast(dict, response)
