from unittest.mock import MagicMock

from pycoingecko.resources.asset_platforms import AssetPlatforms
from pycoingecko.utils import CoinGeckoApiUrls

from ..fixture_data import CoinGeckoAPIFixtureData


def test_asset_platforms_happy() -> None:
    # Arrange
    mock_http = MagicMock(
        send=MagicMock(return_value=CoinGeckoAPIFixtureData.asset_platforms_response())
    )

    # Act
    client = AssetPlatforms(http=mock_http)

    # Assert
    assert (
        client.asset_platforms() == CoinGeckoAPIFixtureData.asset_platforms_response()
    )
    assert mock_http.send.called_once_with(path=CoinGeckoApiUrls.ASSET_PLATFORMS)
