from unittest.mock import MagicMock

from pycoingecko.resources.contract import Contract
from pycoingecko.utils import CoinGeckoApiUrls


def test_contract_coin_data_by_token_address_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Contract(http=mock_http)
    client.coin_data_by_token_address(
        coin_id="ethereum",
        contract_address="0x514910771af9ca656af840dff83e8264ecf986ca",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COINS_CONTRACT_ADDRESS.format(
            id="ethereum", contract_address="0x514910771af9ca656af840dff83e8264ecf986ca"
        )
    )


def test_contract_coin_historical_chart_by_token_address_api_called_with_correct_args() -> (
    None
):
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Contract(http=mock_http)
    client.coin_historical_chart_by_token_address(
        coin_id="ethereum",
        contract_address="0x514910771af9ca656af840dff83e8264ecf986ca",
        vs_currency="usd",
        days="1",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COINS_CONTRACT_CHART_ADDRESS_BY_TOKEN.format(
            id="ethereum",
            contract_address="0x514910771af9ca656af840dff83e8264ecf986ca",
        ),
        params={"vs_currency": "usd", "days": "1"},
    )


def test_contract_coin_historical_chart_range_by_token_address() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Contract(http=mock_http)
    client.coin_historical_chart_range_by_token_address(
        coin_id="ethereum",
        contract_address="0x514910771af9ca656af840dff83e8264ecf986ca",
        vs_currency="usd",
        from_timestamp=1392577232,
        to_timestamp=1422577232,
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.COINS_CONTRACT_CHART_RANGE_ADDRESS_BY_TOKEN.format(
            id="ethereum",
            contract_address="0x514910771af9ca656af840dff83e8264ecf986ca",
        ),
        params={
            "vs_currency": "usd",
            "from": 1392577232,
            "to": 1422577232,
        },
    )
