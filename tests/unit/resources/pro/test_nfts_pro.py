from unittest.mock import MagicMock

from pycoingecko.resources.pro.nfts import NFTsPro
from pycoingecko.utils import CoinGeckoApiUrls


def test_collection_with_market_data_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = NFTsPro(http=mock_http)
    client.collection_with_market_data()

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.NFTS_MARKET, params={"page": 1, "per_page": 100}
    )
