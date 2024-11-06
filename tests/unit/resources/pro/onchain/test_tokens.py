from unittest.mock import MagicMock

from pycoingecko.resources.pro.onchain import TokensOnChain
from pycoingecko.utils import CoinGeckoApiUrls


def test_tokens_top_pools_by_token_address_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = TokensOnChain(http=mock_http)
    client.top_pools_by_token_address(
        network="eth",
        token_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
        include="quote_token",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_TOKENS_TOP_POOLS.format(
            network="eth", token_address="0x06da0fd433c1a5d7a4faa01111c044910a184553"
        ),
        params={"include": "quote_token"},
    )


def test_tokens_data_by_token_address_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = TokensOnChain(http=mock_http)
    client.data_by_token_address(
        network="eth",
        address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
        include="top_pools",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_TOKEN_BY_ADDRESS.format(
            network="eth", address="0x06da0fd433c1a5d7a4faa01111c044910a184553"
        ),
        params={"include": "top_pools"},
    )


def test_tokens_data_by_token_multi_addresses_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = TokensOnChain(http=mock_http)
    client.data_by_token_multi_addresses(
        network="eth",
        addresses="0x06da0fd433c1a5d7a4faa01111c044910a184553,0x514910771af9ca656af840dff83e8264ecf986ca",
        include="top_pools",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_TOKEN_BY_MULTI_ADDRESSES.format(
            network="eth",
            addresses="0x06da0fd433c1a5d7a4faa01111c044910a184553,0x514910771af9ca656af840dff83e8264ecf986ca",
        ),
        params={"include": "top_pools"},
    )


def test_tokens_info_by_token_address_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = TokensOnChain(http=mock_http)
    client.info_by_token_address(
        network="eth",
        address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_TOKEN_INFO_BY_ADDRESS.format(
            network="eth", address="0x06da0fd433c1a5d7a4faa01111c044910a184553"
        )
    )


def test_tokens_pool_tokens_info_by_pool_address_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = TokensOnChain(http=mock_http)
    client.pool_tokens_info_by_pool_address(
        network="eth",
        pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_TOKEN_POOL_INFO_BY_ADDRESS.format(
            network="eth", pool_address="0x06da0fd433c1a5d7a4faa01111c044910a184553"
        )
    )


def test_tokens_most_recently_updated_api_expected_response() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = TokensOnChain(http=mock_http)
    client.most_recently_updated(include="network", network="eth")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.ONCHAIN_TOKEN_MOST_RECENTLY_UPDATED,
        params={"include": "network", "network": "eth"},
    )
