from unittest.mock import MagicMock

from pycoingecko.resources.simple import Simple
from pycoingecko.utils import CoinGeckoApiUrls


def test_simple_price_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Simple(http=mock_http)
    client.coin_price_by_id(ids="bitcoin", vs_currencies="usd")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.PRICE, params={"ids": "bitcoin", "vs_currencies": "usd"}
    )


def test_simple_token_price_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Simple(http=mock_http)
    client.coin_price_by_token(
        asset_id="ethereum",
        contract_addresses="0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
        vs_currencies="usd",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.TOKEN_PRICE.format(id="ethereum"),
        params={
            "contract_addresses": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
            "vs_currencies": "usd",
        },
    )


def test_simple_supported_vs_currencies_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Simple(http=mock_http)
    client.supported_vs_currencies()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.SUPPORTED_CURRENCIES)
