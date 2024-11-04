from unittest.mock import MagicMock

from pycoingecko.resources.pro.global_data import GlobalDataPro
from pycoingecko.utils import CoinGeckoApiUrls


def test_global_cap_chart_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = GlobalDataPro(http=mock_http)
    client.volume_chart_within_time_range(days="1")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.GLOBAL_MARKET_CAP_CHART,
        params={"days": "1", "vs_currency": "usd"},
    )
