from pycoingecko.clients.demo import CoinGeckoDemoClient
from pycoingecko.resources import pro
from pycoingecko.resources.pro import onchain


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

    # On Chain (BETA)
    @property
    def onchain_simple(self) -> onchain.SimpleOnChain:
        return onchain.SimpleOnChain(self.http)

    @property
    def onchain_networks(self) -> onchain.NetworksOnChain:
        return onchain.NetworksOnChain(self.http)

    @property
    def onchain_dexes(self) -> onchain.DexesOnChain:
        return onchain.DexesOnChain(self.http)

    @property
    def onchain_pools(self) -> onchain.PoolsOnChain:
        return onchain.PoolsOnChain(self.http)

    @property
    def onchain_tokens(self) -> onchain.TokensOnChain:
        return onchain.TokensOnChain(self.http)

    @property
    def onchain_ohlcv(self) -> onchain.OHLCVOnChain:
        return onchain.OHLCVOnChain(self.http)

    @property
    def onchain_trades(self) -> onchain.TradesOnChain:
        return onchain.TradesOnChain(self.http)
