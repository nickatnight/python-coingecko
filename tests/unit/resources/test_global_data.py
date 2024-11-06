from unittest.mock import MagicMock

from pycoingecko.resources.global_data import GlobalData
from pycoingecko.utils import CoinGeckoApiUrls


def test_crypto_market_data_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = GlobalData(http=mock_http)
    client.crypto_market_data()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.GLOBAL)


def test_defi_market_data_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = GlobalData(http=mock_http)
    client.defi_market_data()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.GLOBAL_DEFI)
