from unittest.mock import MagicMock

from pycoingecko.resources.exchanges import Exchanges
from pycoingecko.utils import CoinGeckoApiUrls


def test_exchanges_list_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Exchanges(http=mock_http)
    client.exchanges_list()

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.EXCHANGES, params={"per_page": 100, "page": 1}
    )


def test_exchanges_list_id_map_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Exchanges(http=mock_http)
    client.exchanges_list_id_map()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.EXCHANGES_LIST)


def test_exchange_by_id_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Exchanges(http=mock_http)
    client.exchange_by_id(exchange_id="binance")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.EXCHANGE.format(id="binance")
    )


def test_exchange_tickers_by_id_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Exchanges(http=mock_http)
    client.exchange_tickers_by_id(exchange_id="binance")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.EXCHANGE_TICKERS.format(id="binance")
    )


def test_exchange_volume_chart_by_id_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Exchanges(http=mock_http)
    client.exchange_volume_chart_by_id(exchange_id="binance", days=1)

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.EXCHANGE_VOLUME_CHART.format(id="binance"),
        params={"days": 1},
    )
