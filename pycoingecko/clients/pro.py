from pycoingecko.clients.demo import CoinGeckoDemoClient
from pycoingecko.resources import pro


class CoinGeckoProClient(CoinGeckoDemoClient):
    """CoinGecko Pro API Client"""

    @property
    def key(self) -> pro.Key:
        return pro.Key(self.http)

    @property
    def coins(self) -> pro.CoinsPro:
        return pro.CoinsPro(self.http)

    @property
    def asset_platforms(self) -> pro.AssetPlatformsPro:
        return pro.AssetPlatformsPro(self.http)

    @property
    def exchanges(self) -> pro.ExchangesPro:
        return pro.ExchangesPro(self.http)

    @property
    def nfts(self) -> pro.NFTsPro:
        return pro.NFTsPro(self.http)

    @property
    def global_data(self) -> pro.GlobalDataPro:
        return pro.GlobalDataPro(self.http)
