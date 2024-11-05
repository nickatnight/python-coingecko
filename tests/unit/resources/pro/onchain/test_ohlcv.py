from unittest.mock import MagicMock

from pycoingecko.resources.pro.onchain import OHLCVOnChain
from pycoingecko.utils import CoinGeckoApiUrls


def test_ohlcv_chart_by_pool_address_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = OHLCVOnChain(http=mock_http)
    client.chart_by_pool_address(
        network="eth",
        pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
        timeframe="day",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_OHLCV_BY_POOL_ADDRESS.format(
            network="eth",
            pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
            timeframe="day",
        ),
    )
