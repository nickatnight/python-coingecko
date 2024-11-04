from typing import cast

from pycoingecko.resources.asset_platforms import AssetPlatforms
from pycoingecko.utils import CoinGeckoApiUrls


class AssetPlatformsPro(AssetPlatforms):
    def token_list(self, *, asset_platform_id: str) -> dict:
        "Get full list of tokens of a blockchain network (asset platform) that is supported by Ethereum token list standard."
        path = CoinGeckoApiUrls.ASSET_PLATFORMS_TOKEN_LIST.format(
            asset_platform_id=asset_platform_id
        )
        response = self.http.send(path=path)

        return cast(dict, response)
