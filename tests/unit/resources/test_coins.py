from unittest.mock import MagicMock

from pycoingecko.resources.coins import Coins
from pycoingecko.utils import CoinGeckoApiUrls


def test_coins_list_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.coins_list()

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COINS_LIST, params={"include_platform": False}
    )


def test_coins_markets_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.coins_markets(vs_currency="usd")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COINS_MARKETS, params={"vs_currency": "usd"}
    )


def test_coin_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.coin_by_id(coin_id="bitcoin")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN.format(id="bitcoin")
    )


def test_coin_tickers_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.coin_tickers_by_id(coin_id="bitcoin")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_TICKERS.format(id="bitcoin")
    )


def test_coin_history_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.coin_history_by_id(coin_id="bitcoin", snapshot_date="30-12-2011")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_HISTORY.format(id="bitcoin"),
        params={"date": "30-12-2011", "localization": True},
    )


def test_coin_history_chart_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.coin_history_chart_by_id(coin_id="bitcoin", vs_currency="usd")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_HISTORY_CHART.format(id="bitcoin"),
        params={"vs_currency": "usd", "days": "1"},
    )


def test_coin_history_chart_range_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.coin_history_chart_range_by_id(
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


def test_coin_ohlc_by_id_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Coins(http=mock_http)
    client.coin_ohlc_by_id(coin_id="bitcoin")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_OHLC.format(id="bitcoin"),
        params={"vs_currency": "usd", "days": "1"},
    )
