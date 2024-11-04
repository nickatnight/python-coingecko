from unittest.mock import MagicMock

from pycoingecko.resources.categories import Categories
from pycoingecko.utils import CoinGeckoApiUrls


def test_categories_list_happy() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Categories(http=mock_http)
    client.categories_list()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.CATEGORIES)


def test_categories_list_with_market_data_happy() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Categories(http=mock_http)
    client.categories_list_with_market_data(order="market_cap_desc")

    # Assert
    assert mock_http.send.called_once_with(
        path=CoinGeckoApiUrls.CATEGORIES_MARKETS, params={"order": "market_cap_desc"}
    )
