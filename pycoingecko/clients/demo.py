from pycoingecko import resources
from pycoingecko.utils import IHttp


class CoinGeckoDemoClient:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    @property
    def ping(self) -> resources.Ping:
        return resources.Ping(self.http)

    @property
    def simple(self) -> resources.Simple:
        return resources.Simple(self.http)

    @property
    def coins(self) -> resources.Coins:
        return resources.Coins(self.http)

    @property
    def contract(self) -> resources.Contract:
        return resources.Contract(self.http)

    @property
    def asset_platforms(self) -> resources.AssetPlatforms:
        return resources.AssetPlatforms(self.http)

    @property
    def categories(self) -> resources.Categories:
        return resources.Categories(self.http)

    @property
    def exchanges(self) -> resources.Exchanges:
        return resources.Exchanges(self.http)

    @property
    def derivatives(self) -> resources.Derivatives:
        return resources.Derivatives(self.http)

    @property
    def nfts(self) -> resources.NFTs:
        return resources.NFTs(self.http)

    @property
    def exchange_rates(self) -> resources.ExchangeRates:
        return resources.ExchangeRates(self.http)

    @property
    def search(self) -> resources.Search:
        return resources.Search(self.http)

    @property
    def trending(self) -> resources.Trending:
        return resources.Trending(self.http)

    @property
    def global_data(self) -> resources.GlobalData:
        return resources.GlobalData(self.http)

    @property
    def companies(self) -> resources.Companies:
        return resources.Companies(self.http)
