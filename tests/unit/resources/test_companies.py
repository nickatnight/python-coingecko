from unittest.mock import MagicMock

from pycoingecko.resources.companies import Companies
from pycoingecko.utils import CoinGeckoApiUrls


def test_companies_holdings_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Companies(http=mock_http)
    client.holdings(coin_id="ethereum")

    # Assert
    assert mock_http.send.called_once_with(
        path=CoinGeckoApiUrls.COMPANIES.format(coin_id="ethereum")
    )
