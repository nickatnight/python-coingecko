from unittest.mock import MagicMock

from pycoingecko.resources.pro.onchain import TokensOnChain
from pycoingecko.utils import CoinGeckoApiUrls


def test_tokens_top_pools_by_token_address_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = TokensOnChain(http=mock_http)
    client.top_pools_by_token_address(
        network="eth",
        token_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
        include="quote_token",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_TOKENS_TOP_POOLS.format(
            network="eth", token_address="0x06da0fd433c1a5d7a4faa01111c044910a184553"
        ),
        params={"include": "quote_token"},
    )
