from pycoingecko import resources
from pycoingecko.clients.demo import CoinGeckoDemoClient
from pycoingecko.resources import pro


class CoinGeckoProClient(CoinGeckoDemoClient):
    """CoinGecko Pro API Client"""

    @property
    def coins(self) -> pro.CoinsPro:
        return pro.CoinsPro(self.http)

    @property
    def asset_platforms(self) -> resources.AssetPlatforms:
        return resources.AssetPlatforms(self.http)

    @property
    def exchanges(self) -> pro.ExchangesPro:
        return pro.ExchangesPro(self.http)

    @property
    def global_market(self) -> pro.GlobalDataPro:
        return pro.GlobalDataPro(self.http)
