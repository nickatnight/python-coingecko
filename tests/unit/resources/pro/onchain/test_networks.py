from unittest.mock import MagicMock

from pycoingecko.resources.pro.onchain import NetworksOnChain
from pycoingecko.utils import CoinGeckoApiUrls


def test_dexes_network_list_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = NetworksOnChain(http=mock_http)
    client.networks_list(page=1)

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_NETWORKS, params={"page": 1}
    )
