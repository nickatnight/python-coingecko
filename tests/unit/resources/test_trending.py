from unittest.mock import MagicMock

from pycoingecko.resources.trending import Trending
from pycoingecko.utils import CoinGeckoApiUrls


def test_trending_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Trending(http=mock_http)
    client.search()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.TRENDING)
