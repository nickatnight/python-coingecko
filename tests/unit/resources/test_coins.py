from unittest.mock import MagicMock

from pycoingecko.resources.coins import Coins
from pycoingecko.utils import CoinGeckoApiUrls

from ..fixture_data import CoinGeckoAPIFixtureData


def test_coins_list_api_expected_response() -> None:
    # Arrange
    data = CoinGeckoAPIFixtureData.coins_list_response()
    mock_http = MagicMock(send=MagicMock(return_value=data))

    # Act
    client = Coins(http=mock_http)

    # Assert
    assert client.coins_list() == data
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COINS_LIST, params={"include_platform": False}
    )


def test_coins_markets_api_expected_response() -> None:
    # Arrange
    data = CoinGeckoAPIFixtureData.coins_markets_response()
    mock_http = MagicMock(send=MagicMock(return_value=data))

    # Act
    client = Coins(http=mock_http)

    # Assert
    assert client.coins_markets(vs_currency="usd") == data
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COINS_MARKETS, params={"vs_currency": "usd"}
    )


def test_coin_by_id_api_expected_response() -> None:
    # Arrange
    data = CoinGeckoAPIFixtureData.coin_by_id_response()
    mock_http = MagicMock(send=MagicMock(return_value=data))

    # Act
    client = Coins(http=mock_http)

    # Assert
    assert client.coin_by_id(coin_id="bitcoin") == data
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN.format(id="bitcoin")
    )


def test_coin_history_by_id_api_expected_response() -> None:
    # Arrange
    data = CoinGeckoAPIFixtureData.coin_history_by_id_response()
    mock_http = MagicMock(send=MagicMock(return_value=data))

    # Act
    client = Coins(http=mock_http)

    # Assert
    assert (
        client.coin_history_by_id(coin_id="bitcoin", snapshot_date="30-12-2011") == data
    )
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_HISTORY.format(id="bitcoin"),
        params={"date": "30-12-2011", "localization": True},
    )


def test_coin_history_chart_range_by_id_api_expected_response() -> None:
    # Arrange
    data = CoinGeckoAPIFixtureData.coin_history_by_id_response()
    mock_http = MagicMock(send=MagicMock(return_value=data))

    # Act
    client = Coins(http=mock_http)

    # Assert
    assert (
        client.coin_history_chart_by_id(coin_id="bitcoin", vs_currency="usd", days="1")
        == data
    )
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_HISTORY_CHART.format(id="bitcoin"),
        params={"vs_currency": "usd", "days": "1"},
    )


def test_coin_ohlc_by_id_api_expected_response() -> None:
    # Arrange
    data = CoinGeckoAPIFixtureData.coin_ohlc_by_id_response()
    mock_http = MagicMock(send=MagicMock(return_value=data))

    # Act
    client = Coins(http=mock_http)

    # Assert
    assert client.coin_ohlc_by_id(coin_id="bitcoin") == data
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COIN_OHLC.format(id="bitcoin"),
        params={"vs_currency": "usd", "days": "1"},
    )
