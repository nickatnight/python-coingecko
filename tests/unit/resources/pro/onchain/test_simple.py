from unittest.mock import MagicMock

from pycoingecko.resources.pro.onchain import SimpleOnChain
from pycoingecko.utils import CoinGeckoApiUrls


def test_simple_token_price_by_address_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = SimpleOnChain(http=mock_http)
    client.token_price_by_address(
        network="eth", addresses="0x06da0fd433c1a5d7a4faa01111c044910a184553"
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_TOKEN_PRICE_BY_ADDRESS.format(
            network="eth",
            addresses="0x06da0fd433c1a5d7a4faa01111c044910a184553",
            timeframe="day",
        ),
    )
