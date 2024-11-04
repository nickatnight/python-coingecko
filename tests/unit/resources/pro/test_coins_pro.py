from unittest.mock import MagicMock

from pycoingecko.resources.pro.coins import CoinsPro
from pycoingecko.utils import CoinGeckoApiUrls


def test_coins_top_gainers_and_losers_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = CoinsPro(http=mock_http)
    client.top_gainers_and_losers(vs_currency="bitcoin")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_TOP_GAINERS_AND_LOSERS,
        params={"vs_currency": "bitcoin"},
    )


def test_coins_recently_added_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = CoinsPro(http=mock_http)
    client.recently_added()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.COIN_RECENTLY_ADDED)


def test_coins_ohlc_chart_within_time_range_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = CoinsPro(http=mock_http)
    client.ohlc_chart_within_time_range(
        coin_id="bitcoin",
        vs_currency="usd",
        from_timestamp=1620000000,
        to_timestamp=1620000000,
        interval="daily",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_OHLC_CHART_TIME_RANGE.format(id="bitcoin"),
        params={
            "vs_currency": "usd",
            "from": 1620000000,
            "to": 1620000000,
            "interval": "daily",
        },
    )


def test_coins_circulating_supply_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = CoinsPro(http=mock_http)
    client.circulating_supply(coin_id="bitcoin", days="1")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_CIRCULATING_SUPPLY.format(coin_id="bitcoin"),
        params={"days": "1"},
    )


def test_coins_circulating_supply_within_time_range_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = CoinsPro(http=mock_http)
    client.circulating_supply_within_time_range(
        coin_id="bitcoin",
        from_timestamp=1620000000,
        to_timestamp=1620000000,
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_CIRCULATING_SUPPLY_TIME_RANGE.format(id="bitcoin"),
        params={"from": 1620000000, "to": 1620000000},
    )


def test_coins_total_supply_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = CoinsPro(http=mock_http)
    client.total_supply(coin_id="bitcoin", days="1")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_TOTAL_SUPPLY.format(id="bitcoin"),
        params={"days": "1"},
    )


def test_coins_total_supply_within_time_range_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = CoinsPro(http=mock_http)
    client.total_supply_within_time_range(
        coin_id="bitcoin",
        from_timestamp=1620000000,
        to_timestamp=1620000000,
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_TOTAL_SUPPLY_TIME_RANGE.format(id="bitcoin"),
        params={"from": 1620000000, "to": 1620000000},
    )
