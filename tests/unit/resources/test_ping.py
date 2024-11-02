from unittest.mock import MagicMock

from pycoingecko.resources.ping import Ping

from ..fixture_data import CoinGeckoAPIFixtureData


def test_ping_api_happy() -> None:
    # Arrange
    mock_http = MagicMock(
        send=MagicMock(return_value=CoinGeckoAPIFixtureData.ping_response())
    )

    # Act
    client = Ping(http=mock_http)

    # Assert
    assert client.ping() == CoinGeckoAPIFixtureData.ping_response()
