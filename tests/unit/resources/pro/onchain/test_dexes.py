from unittest.mock import MagicMock

from pycoingecko.resources.pro.onchain import DexesOnChain
from pycoingecko.utils import CoinGeckoApiUrls


def test_dexes_network_list_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DexesOnChain(http=mock_http)
    client.networks_list(network="eth")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_DEXES_BY_NETWORK.format(network="eth"),
        params={"page": 1},
    )
