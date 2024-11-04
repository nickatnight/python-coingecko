from unittest.mock import MagicMock

from pycoingecko.resources.ping import Ping
from pycoingecko.utils import CoinGeckoApiUrls


def test_ping_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Ping(http=mock_http)
    client.ping()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.PING)
