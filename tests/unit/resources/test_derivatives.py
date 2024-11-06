from unittest.mock import MagicMock

from pycoingecko.resources.derivatives import Derivatives
from pycoingecko.utils import CoinGeckoApiUrls


def test_derivatives_ticker_list_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Derivatives(http=mock_http)
    client.ticker_list()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.DERIVATIVES_TICKERS)


def test_derivatives_exchanges_list_with_data_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Derivatives(http=mock_http)
    client.exchanges_list_with_data()

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.DERIVATIVES_EXCHANGES,
        params={"order": "open_interest_btc_desc", "per_page": 100, "page": 1},
    )


def test_derivatives_by_id_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Derivatives(http=mock_http)
    client.by_id(exchange_id="bitmex", include_tickers="all")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.DERIVATIVES_EXCHANGE.format(id="bitmex"),
        params={"include_tickers": "all"},
    )


def test_derivatives_list_id_map_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Derivatives(http=mock_http)
    client.list_id_map()

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.DERIVATIVES_EXCHANGE_LIST
    )
