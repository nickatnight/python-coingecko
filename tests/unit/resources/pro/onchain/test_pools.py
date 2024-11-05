from unittest.mock import MagicMock

from pycoingecko.resources.pro.onchain import PoolsOnChain
from pycoingecko.utils import CoinGeckoApiUrls


def test_pools_trending_list_list_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = PoolsOnChain(http=mock_http)
    client.trending_list(include="base_token")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_TRENDING_POOLS,
        params={"include": "base_token", "page": 1},
    )


def test_pools_trending_list_by_network_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = PoolsOnChain(http=mock_http)
    client.trending_list_by_network(network="eth", include="base_token")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_POOLS_TRENDING_BY_NETWORK.format(network="eth"),
        params={"include": "base_token", "page": 1},
    )


def test_pools_data_by_pool_address() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = PoolsOnChain(http=mock_http)
    client.data_by_pool_address(
        network="eth", pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553"
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_POOL_BY_ADDRESS.format(
            network="eth", address="0x06da0fd433c1a5d7a4faa01111c044910a184553"
        )
    )
