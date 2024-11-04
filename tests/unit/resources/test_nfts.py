from unittest.mock import MagicMock

from pycoingecko.resources.nfts import NFTs
from pycoingecko.utils import CoinGeckoApiUrls


def test_nft_list_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = NFTs(http=mock_http)
    client.nft_list(order="h24_volume_usd_asc")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.NFTS,
        params={"order": "h24_volume_usd_asc", "page": 1, "per_page": 100},
    )


def test_nfts_collection_by_id_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = NFTs(http=mock_http)
    client.collection_by_id(collection_id="nifty-gateway")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.NFTS_COLLECTION.format(id="nifty-gateway")
    )


def test_collection_by_contract_address_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = NFTs(http=mock_http)
    client.collection_by_contract_address(
        asset_platform_id="popcat",
        contract_address="0x06012c8cf97bead5deae237070f9587f8e7a266d",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.NFTS_COLLECTION_CONTRACT_ADDRESS.format(
            asset_platform_id="popcat",
            contract_address="0x06012c8cf97bead5deae237070f9587f8e7a266d",
        )
    )
