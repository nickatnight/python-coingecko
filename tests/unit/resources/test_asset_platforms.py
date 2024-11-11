from unittest.mock import MagicMock

from pycoingecko.resources.asset_platforms import AssetPlatforms
from pycoingecko.utils import CoinGeckoApiUrls


def test_asset_platforms_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = AssetPlatforms(http=mock_http)
    client.list_id_map(filters="nft")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ASSET_PLATFORMS, params={"filters": "nft"}
    )
