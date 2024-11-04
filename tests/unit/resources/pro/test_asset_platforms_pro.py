from unittest.mock import MagicMock

from pycoingecko.resources.pro.asset_platforms import AssetPlatformsPro
from pycoingecko.utils import CoinGeckoApiUrls


def test_asset_platforms_token_list_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = AssetPlatformsPro(http=mock_http)
    client.token_list(asset_platform_id="bitcoin")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ASSET_PLATFORMS_TOKEN_LIST.format(
            asset_platform_id="bitcoin"
        ),
    )
