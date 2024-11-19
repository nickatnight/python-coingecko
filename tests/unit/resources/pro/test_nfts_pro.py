from unittest.mock import MagicMock

from pycoingecko.resources.pro.nfts import NFTsPro
from pycoingecko.utils import CoinGeckoApiUrls


def test_collection_with_market_data_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = NFTsPro(http=mock_http)
    client.collection_with_market_data(asset_platform_id="ethereum")

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.NFTS_MARKET,
        params={
            "asset_platform_id": "ethereum",
            "order": "market_cap_usd_desc",
            "per_page": 100,
            "page": 1,
        },
    )


def test_historical_chart_by_id_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = NFTsPro(http=mock_http)
    client.historical_chart_by_id(
        nft_id="nifty-gateway",
        days="1",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.NFTS_HISTORICAL_CHART.format(id="nifty-gateway"),
        params={"days": "1"},
    )


def test_historical_chart_by_contract_address_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = NFTsPro(http=mock_http)
    client.historical_chart_by_contract_address(
        asset_platform_id="ethereum",
        contract_address="0x495f947276749ce646f68ac8c248420045cb7b5e",
        days="1",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.NFTS_HISTORICAL_CHART_BY_ADDRESS.format(
            asset_platform_id="ethereum",
            contract_address="0x495f947276749ce646f68ac8c248420045cb7b5e",
        ),
        params={"days": "1"},
    )


def test_tickers_by_id_api_called_with_correct_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = NFTsPro(http=mock_http)
    client.tickers_by_id(
        nft_id="nifty-gateway",
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=CoinGeckoApiUrls.NFTS_TICKERS_BY_ID.format(id="nifty-gateway")
    )
