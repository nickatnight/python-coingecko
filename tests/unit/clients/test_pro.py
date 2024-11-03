from typing import Any
from unittest.mock import MagicMock

import pytest

from pycoingecko import resources
from pycoingecko.clients.pro import CoinGeckoProClient
from pycoingecko.resources import pro
from pycoingecko.utils.helpers import get_client_api_methods


@pytest.mark.parametrize(
    "method_name,class_instance",
    [
        ("ping", resources.Ping),
        ("simple", resources.Simple),
        ("coins", pro.CoinsPro),
        ("contract", resources.Contract),
        ("asset_platforms", resources.AssetPlatforms),
        ("categories", resources.Categories),
        ("exchanges", pro.ExchangesPro),
        ("derivatives", resources.Derivatives),
        ("exchange_rates", resources.ExchangeRates),
        ("search", resources.Search),
        ("trending", resources.Trending),
        ("global_data", pro.GlobalDataPro),
    ],
)
def test_ping_called_with_correct_args(method_name: str, class_instance: Any) -> None:
    # Arrange
    client = CoinGeckoProClient(http=MagicMock())

    # Act / Assert
    assert isinstance(getattr(client, method_name), class_instance)


def test_supported_methods_count() -> None:
    # Arrange
    client = CoinGeckoProClient(http=MagicMock())

    # Act / Assert
    assert len(get_client_api_methods(client=client)) == 13
