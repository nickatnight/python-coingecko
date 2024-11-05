from pycoingecko.coingecko import CoinGecko


def test_client_with_defaults() -> None:
    # Arrange
    client = CoinGecko(api_key="test")

    # Act / Assert
    assert client is not None
