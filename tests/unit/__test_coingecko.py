# mypy: disable-error-code="attr-defined"
from unittest.mock import MagicMock

from pycoingecko import resources
from pycoingecko.coingecko import CoinGecko


def test_ping_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_ping = mocker.patch.object(resources.Ping, "ping", return_value=MagicMock())
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.ping_check_server_status()

    # Assert
    mock_ping.assert_called_once()


def test_simple_coin_price_by_id_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_coin_price_by_id = mocker.patch.object(
        resources.Simple, "coin_price_by_id", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.simple_coin_price_by_id("bitcoin", "usd")

    # Assert
    mock_coin_price_by_id.assert_called_once_with(
        request={"params": {"ids": "bitcoin", "vs_currencies": "usd"}}
    )


def test_simple_coin_price_by_token_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_coin_price_by_id = mocker.patch.object(
        resources.Simple, "coin_price_by_token", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.simple_coin_price_by_token("ethereum", "0xl33t", "usd")

    # Assert
    mock_coin_price_by_id.assert_called_once_with(
        asset_id="ethereum",
        request={"params": {"contract_address": "0xl33t", "vs_currencies": "usd"}},
    )


def test_simple_supported_vs_currencies_called_with_correct_args(
    mocker: MagicMock,
) -> None:
    # Arrange
    mock_supported_vs_currencies = mocker.patch.object(
        resources.Simple, "supported_vs_currencies", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.simple_supported_vs_currencies()

    # Assert
    mock_supported_vs_currencies.assert_called_once()


def test_coins_list_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_coins_list = mocker.patch.object(
        resources.Coins, "coins_list", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.coins_list()

    # Assert
    mock_coins_list.assert_called_once_with(
        request={"params": {"include_platform": False}}
    )


def test_coins_markets_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_coins_markets = mocker.patch.object(
        resources.Coins, "coins_markets", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.coins_markets("usd")

    # Assert
    mock_coins_markets.assert_called_once_with(
        request={"params": {"vs_currency": "usd"}}
    )


def test_coin_by_id_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_coin_by_id = mocker.patch.object(
        resources.Coins, "coin_by_id", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.coin_by_id("bitcoin")

    # Assert
    mock_coin_by_id.assert_called_once_with(coin_id="bitcoin", request={"params": {}})


def test_coin_tickers_by_id_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_coin_tickers_by_id = mocker.patch.object(
        resources.Coins, "coin_tickers_by_id", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.coin_tickers_by_id("bitcoin")

    # Assert
    mock_coin_tickers_by_id.assert_called_once_with(
        coin_id="bitcoin", request={"params": {}}
    )


def test_coin_history_by_id_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_coin_history_by_id = mocker.patch.object(
        resources.Coins, "coin_history_by_id", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.coin_history_by_id("bitcoin", "2021-01-01")

    # Assert
    mock_coin_history_by_id.assert_called_once_with(
        coin_id="bitcoin",
        request={"params": {"date": "2021-01-01", "localization": True}},
    )


def test_coin_history_chart_by_id_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_coin_history_chart_by_id = mocker.patch.object(
        resources.Coins, "coin_history_chart_by_id", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.coin_history_chart_by_id("bitcoin", "usd")

    # Assert
    mock_coin_history_chart_by_id.assert_called_once_with(
        coin_id="bitcoin", request={"params": {"vs_currency": "usd", "days": "1"}}
    )


def test_coin_history_chart_range_by_id_called_with_correct_args(
    mocker: MagicMock,
) -> None:
    # Arrange
    mock_coin_history_chart_range_by_id = mocker.patch.object(
        resources.Coins,
        "coin_history_chart_range_by_id",
        return_value=MagicMock(),
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.coin_history_chart_range_by_id("bitcoin", "usd", 1609459200, 1609545600)

    # Assert
    mock_coin_history_chart_range_by_id.assert_called_once_with(
        coin_id="bitcoin",
        request={
            "params": {"vs_currency": "usd", "from": 1609459200, "to": 1609545600}
        },
    )


def test_coin_ohlc_by_id_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_coin_ohlc_by_id = mocker.patch.object(
        resources.Coins, "coin_ohlc_by_id", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.coin_ohlc_by_id("bitcoin", "usd")

    # Assert
    mock_coin_ohlc_by_id.assert_called_once_with(
        coin_id="bitcoin", request={"params": {"vs_currency": "usd", "days": "1"}}
    )


def test_coin_data_by_token_address_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_contract_coin_data_by_token_address = mocker.patch.object(
        resources.Contract, "coin_data_by_token_address", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.contract_coin_data_by_token_address("bitcoin", "0xl33t")

    # Assert
    mock_contract_coin_data_by_token_address.assert_called_once_with(
        coin_id="bitcoin", contract_address="0xl33t"
    )


def test_contract_coin_historical_chart_by_token_address_called_with_correct_args(
    mocker: MagicMock,
) -> None:
    # Arrange
    mock_contract_coin_historical_chart_by_token_address = mocker.patch.object(
        resources.Contract,
        "coin_historical_chart_by_token_address",
        return_value=MagicMock(),
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.contract_coin_historical_chart_by_token_address(
        "bitcoin", "0xl33t", "usd"
    )

    # Assert
    mock_contract_coin_historical_chart_by_token_address.assert_called_once_with(
        coin_id="bitcoin",
        contract_address="0xl33t",
        request={"params": {"vs_currency": "usd", "days": "1"}},
    )


def test_contract_coin_historical_chart_range_by_token_address_called_with_correct_args(
    mocker: MagicMock,
) -> None:
    # Arrange
    mock_contract_coin_historical_chart_range_by_token_address = mocker.patch.object(
        resources.Contract,
        "coin_historical_chart_range_by_token_address",
        return_value=MagicMock(),
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.contract_coin_historical_chart_range_by_token_address(
        "bitcoin", "0xl33t", "usd", 1609459200, 1609545600
    )

    # Assert
    mock_contract_coin_historical_chart_range_by_token_address.assert_called_once_with(
        coin_id="bitcoin",
        contract_address="0xl33t",
        request={
            "params": {"vs_currency": "usd", "from": 1609459200, "to": 1609545600}
        },
    )


def test_asset_platforms_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_asset_platforms = mocker.patch.object(
        resources.AssetPlatforms, "asset_platforms", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.assets_platforms()

    # Assert
    mock_asset_platforms.assert_called_once()


def test_categories_list_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_categories_list = mocker.patch.object(
        resources.Categories, "categories_list", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.categories_list()

    # Assert
    mock_categories_list.assert_called_once()


def test_categories_list_with_markets_called_with_correct_args(
    mocker: MagicMock,
) -> None:
    # Arrange
    mock_categories_list_with_markets = mocker.patch.object(
        resources.Categories,
        "categories_list_with_market_data",
        return_value=MagicMock(),
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.categories_with_markets("test")

    # Assert
    mock_categories_list_with_markets.assert_called_once_with(
        request={"params": {"order": "test"}}
    )


def test_exchange_list_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_exchange_list = mocker.patch.object(
        resources.Exchanges, "exchanges_list", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.exchanges_list(100, 1)

    # Assert
    mock_exchange_list.assert_called_once_with(
        request={"params": {"per_page": 100, "page": 1}}
    )


def test_exchanges_list_id_map_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_exchanges_list_id_map = mocker.patch.object(
        resources.Exchanges, "exchanges_list_id_map", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.exchanges_list_id_map()

    # Assert
    mock_exchanges_list_id_map.assert_called_once()


def test_exchange_by_id_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_exchange_by_id = mocker.patch.object(
        resources.Exchanges, "exchange_by_id", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.exchange_by_id("test")

    # Assert
    mock_exchange_by_id.assert_called_once_with(exchange_id="test")


def test_exchange_tickers_by_id_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_exchange_tickers_by_id = mocker.patch.object(
        resources.Exchanges, "exchange_tickers_by_id", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.exchange_tickers_by_id("test")

    # Assert
    mock_exchange_tickers_by_id.assert_called_once_with(
        exchange_id="test", request={"params": {}}
    )


def test_exchange_volume_chart_by_id_called_with_correct_args(
    mocker: MagicMock,
) -> None:
    # Arrange
    mock_exchange_volume_chart_by_id = mocker.patch.object(
        resources.Exchanges,
        "exchange_volume_chart_by_id",
        return_value=MagicMock(),
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.exchange_volume_chart_by_id("test")

    # Assert
    mock_exchange_volume_chart_by_id.assert_called_once_with(
        exchange_id="test", request={"params": {"days": 1}}
    )


def test_derivatives_ticker_list_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_derivatives_ticker_list = mocker.patch.object(
        resources.Derivatives, "ticker_list", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.derivatives_ticker_list()

    # Assert
    mock_derivatives_ticker_list.assert_called_once()


def test_derivatives_exchanges_list_with_data_called_with_correct_args(
    mocker: MagicMock,
) -> None:
    # Arrange
    mock_exchanges_list_with_data = mocker.patch.object(
        resources.Derivatives,
        "exchanges_list_with_data",
        return_value=MagicMock(),
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.derivatives_exchanges_list_with_data()

    # Assert
    mock_exchanges_list_with_data.assert_called_once_with(
        request={
            "params": {"order": "open_interest_btc_desc", "per_page": 100, "page": 1}
        }
    )


def test_derivatives_exchange_by_id_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_exchange_by_id = mocker.patch.object(
        resources.Derivatives, "exchange_by_id", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.derivatives_exchange_by_id("test")

    # Assert
    mock_exchange_by_id.assert_called_once_with(exchange_id="test")


def test_derivative_exchanges_list_id_map_called_with_correct_args(
    mocker: MagicMock,
) -> None:
    # Arrange
    mock_exchanges_list_id_map = mocker.patch.object(
        resources.Derivatives, "exchanges_list_id_map", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.derivatives_exchanges_list_id_map()

    # Assert
    mock_exchanges_list_id_map.assert_called_once()


def test_exchange_rates_btc_to_currency_called_with_correct_args(
    mocker: MagicMock,
) -> None:
    # Arrange
    mock_exchange_rates_btc_to_currency = mocker.patch.object(
        resources.ExchangeRates, "btc_to_currency", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.btc_exchange_rates()

    # Assert
    mock_exchange_rates_btc_to_currency.assert_called_once_with()


def test_search_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_search = mocker.patch.object(
        resources.Search, "search", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.search("test")

    # Assert
    mock_search.assert_called_once_with(request={"params": {"query": "test"}})


def test_trending_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_trending = mocker.patch.object(
        resources.Trending, "trending", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.trending()

    # Assert
    mock_trending.assert_called_once()


def test_global_market_data_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_global_market_data = mocker.patch.object(
        resources.GlobalData, "global_market", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.global_market_data()

    # Assert
    mock_global_market_data.assert_called_once()


def test_global_defi_data_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_global_defi_data = mocker.patch.object(
        resources.GlobalData, "global_defi_market", return_value=MagicMock()
    )
    coin_gecko = CoinGecko(api_key="test")

    # Act
    coin_gecko.global_defi_market_data()

    # Assert
    mock_global_defi_data.assert_called_once()
