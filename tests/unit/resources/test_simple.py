from unittest.mock import MagicMock

from pycoingecko.resources.simple import Simple

from ..fixture_data import CoinGeckoAPIFixtureData


def test_simple_price_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock(
        send=MagicMock(return_value=CoinGeckoAPIFixtureData.simple_price_api_response())
    )

    # Act
    client = Simple(http=mock_http)

    # Assert
    assert (
        client.coin_price_by_id(ids="bitcoin", vs_currencies="usd")
        == CoinGeckoAPIFixtureData.simple_price_api_response()
    )


def test_simple_token_price_api_expected_response() -> None:
    # Arrange
    data = CoinGeckoAPIFixtureData.simple_token_price_api_response()
    mock_http = MagicMock(send=MagicMock(return_value=data))

    # Act
    client = Simple(http=mock_http)

    # Assert
    assert (
        client.coin_price_by_token(
            asset_id="ethereum",
            contract_address="0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
            vs_currencies="usd",
        )
        == data
    )


def test_simple_supported_vs_currencies_api_expected_response() -> None:
    # Arrange
    data: list = []
    mock_http = MagicMock(send=MagicMock(return_value=data))

    # Act
    client = Simple(http=mock_http)

    # Assert
    assert client.supported_vs_currencies() == data
