from unittest.mock import MagicMock

from pycoingecko.resources.categories import Categories
from pycoingecko.utils import CoinGeckoApiUrls

from ..fixture_data import CoinGeckoAPIFixtureData


def test_categories_list_happy() -> None:
    # Arrange
    mock_http = MagicMock(
        send=MagicMock(return_value=CoinGeckoAPIFixtureData.categories_response())
    )

    # Act
    client = Categories(http=mock_http)

    # Assert
    assert client.categories_list() == CoinGeckoAPIFixtureData.categories_response()
    assert mock_http.send.called_once_with(path=CoinGeckoApiUrls.CATEGORIES)


def test_categories_list_with_market_data_happy() -> None:
    # Arrange
    mock_http = MagicMock(
        send=MagicMock(
            return_value=CoinGeckoAPIFixtureData.categories_with_market_data_response()
        )
    )

    # Act
    client = Categories(http=mock_http)

    # Assert
    assert (
        client.categories_list_with_market_data()
        == CoinGeckoAPIFixtureData.categories_with_market_data_response()
    )
    assert mock_http.send.called_once_with(path=CoinGeckoApiUrls.CATEGORIES_MARKETS)
