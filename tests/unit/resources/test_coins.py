from unittest.mock import MagicMock

from pycoingecko.resources.coins import Coins
from pycoingecko.utils import CoinGeckoApiUrls


def test_list_all_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.list_all(include_platform=True)

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COINS_LIST, params={"include_platform": "true"}
    )


def test_list_with_markets_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.list_with_markets(vs_currency="usd")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COINS_MARKETS, params={"vs_currency": "usd"}
    )


def test_data_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.data_by_id(coin_id="bitcoin", localization=False, tickers=False)

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN.format(id="bitcoin"),
        params={"localization": "false", "tickers": "false"},
    )


def test_tickers_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.tickers_by_id(
        coin_id="bitcoin", exchange_ids="binance", include_exchange_logo=True
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_TICKERS.format(id="bitcoin"),
        params={"exchange_ids": "binance", "include_exchange_logo": "true"},
    )


def test_historical_data_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.historical_data_by_id(
        coin_id="bitcoin", snapshot_date="30-12-2011", localization=True
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_HISTORY.format(id="bitcoin"),
        params={"date": "30-12-2011", "localization": "true"},
    )


def test_historical_chart_data_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.historical_chart_data_by_id(coin_id="bitcoin", vs_currency="usd")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_HISTORY_CHART.format(id="bitcoin"),
        params={"vs_currency": "usd", "days": "1"},
    )


def test_historical_chart_data_within_time_range_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.historical_chart_data_within_time_range_by_id(
        coin_id="bitcoin",
        vs_currency="usd",
        from_timestamp=1392577232,
        to_timestamp=1422577232,
        precision="2",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_HISTORY_TIME_RANGE.format(id="bitcoin"),
        params={
            "vs_currency": "usd",
            "from": 1392577232,
            "to": 1422577232,
            "precision": "2",
        },
    )


def test_ohlc_chart_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.ohlc_chart_by_id(coin_id="bitcoin", interval="daily", precision="2")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_OHLC.format(id="bitcoin"),
        params={
            "vs_currency": "usd",
            "days": "1",
            "interval": "daily",
            "precision": "2",
        },
    )
