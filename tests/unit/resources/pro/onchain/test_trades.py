from unittest.mock import MagicMock

from pycoingecko.resources.pro.onchain import TradesOnChain
from pycoingecko.utils import CoinGeckoApiUrls


def test_trades_past_24_hour_trades_by_pool_address_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = TradesOnChain(http=mock_http)
    client.past_24_hour_trades_by_pool_address(
        network="eth", pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553"
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_TRADES_BY_POOL_ADDRESS.format(
            network="eth", pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553"
        ),
        params={"trade_volume_in_usd_greater_than": 0},
    )
