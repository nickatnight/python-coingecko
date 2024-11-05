from typing import Any
from unittest.mock import MagicMock

import pytest

from pycoingecko import resources
from pycoingecko.clients.pro import CoinGeckoProClient
from pycoingecko.resources import pro
from pycoingecko.resources.pro import onchain
from pycoingecko.utils.helpers import get_client_api_methods


@pytest.mark.parametrize(
    "method_name,class_instance",
    [
        ("key", pro.Key),
        ("ping", resources.Ping),
        ("simple", resources.Simple),
        ("coins", pro.CoinsPro),
        ("contract", resources.Contract),
        ("asset_platforms", pro.AssetPlatformsPro),
        ("categories", resources.Categories),
        ("exchanges", pro.ExchangesPro),
        ("nfts", pro.NFTsPro),
        ("companies", resources.Companies),
        ("derivatives", resources.Derivatives),
        ("exchange_rates", resources.ExchangeRates),
        ("search", resources.Search),
        ("trending", resources.Trending),
        ("global_data", pro.GlobalDataPro),
        ("onchain_simple", onchain.SimpleOnChain),
        ("onchain_networks", onchain.NetworksOnChain),
        ("onchain_dexes", onchain.DexesOnChain),
        ("onchain_pools", onchain.PoolsOnChain),
        ("onchain_tokens", onchain.TokensOnChain),
        ("onchain_ohlcv", onchain.OHLCVOnChain),
        ("onchain_trades", onchain.TradesOnChain),
    ],
)
def test_api_method_invokes_correct_class(
    method_name: str, class_instance: Any
) -> None:
    # Arrange
    client = CoinGeckoProClient(http=MagicMock())

    # Act / Assert
    assert getattr(client, method_name).__class__.__name__ == class_instance.__name__


def test_supported_methods_count() -> None:
    # Arrange
    client = CoinGeckoProClient(http=MagicMock())

    # Act / Assert
    assert len(get_client_api_methods(client=client)) == 22
