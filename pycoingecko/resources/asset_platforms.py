from typing import Optional, cast

from pycoingecko.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class AssetPlatforms:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def list_id_map(self, filters: Optional[str] = None) -> list:
        """Query all the asset platforms on CoinGecko

        :param filters:     Apply relevant filters to results
        """
        request: CoinGeckoRequestParams = {}

        if filters:
            params = {"filters": filters}
            request = {"params": params}

        response = self.http.send(path=CoinGeckoApiUrls.ASSET_PLATFORMS, **request)

        return cast(list, response)
