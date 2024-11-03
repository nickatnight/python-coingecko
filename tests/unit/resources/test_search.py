from unittest.mock import MagicMock

from pycoingecko.resources.search import Search
from pycoingecko.utils import CoinGeckoApiUrls


def test_search_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Search(http=mock_http)
    client.search()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.SEARCH)
