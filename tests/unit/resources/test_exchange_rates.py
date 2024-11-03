from unittest.mock import MagicMock

from pycoingecko.resources.exchange_rates import ExchangeRates
from pycoingecko.utils import CoinGeckoApiUrls


def test_exchange_rates_btc_to_currency_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = ExchangeRates(http=mock_http)
    client.btc_to_currency()

    # Assert
    mock_http.send.assert_called_once_with(path=CoinGeckoApiUrls.BTC_TO_CURRENCY)
