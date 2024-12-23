from unittest.mock import MagicMock

from pycoingecko.resources.pro.key import Key
from pycoingecko.utils import CoinGeckoApiUrls


def test_coins_key_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Key(http=mock_http)
    client.api_usage()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.KEY)
