from unittest.mock import MagicMock

from pycoingecko.resources.pro.exchanges import ExchangesPro
from pycoingecko.utils import CoinGeckoApiUrls


def test_volume_chart_within_time_range_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = ExchangesPro(http=mock_http)
    client.volume_chart_within_time_range(
        exchange_id="binance", from_timestamp=1514764800, to_timestamp=1514764800
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.EXCHANGE_VOLUME_CHART_TIME_RANGE.format(id="binance"),
        params={"from": 1514764800, "to": 1514764800},
    )
