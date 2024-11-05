from unittest.mock import MagicMock

import pytest

from pycoingecko.clients.demo import CoinGeckoDemoClient
from pycoingecko.clients.pro import CoinGeckoProClient
from pycoingecko.coingecko import CoinGecko, __version__
from pycoingecko.utils import DEMO_COIN_GECKO_API_URL, PRO_COIN_GECKO_API_URL


def test_client_with_defaults() -> None:
    # Arrange
    client = CoinGecko(api_key="test")

    # Act / Assert
    assert client is not None


@pytest.mark.parametrize(
    "client_class, is_pro, header, url",
    [
        (CoinGeckoDemoClient, False, "x-cg-demo-api-key", DEMO_COIN_GECKO_API_URL),
        (CoinGeckoProClient, True, "x-cg-pro-api-key", PRO_COIN_GECKO_API_URL),
    ],
)
def test_correct_clients_get_invoked(
    mocker: MagicMock, client_class: object, is_pro: bool, header: str, url: str
) -> None:
    # Arrange
    mock_get_client = mocker.patch("pycoingecko.coingecko.get_client_api_methods")
    mock_http = mocker.patch("pycoingecko.coingecko.RequestsClient")

    # Act
    _ = CoinGecko(api_key="test", is_pro=is_pro)

    # Assert
    mock_get_client.assert_called_once_with(client=client_class)
    mock_http.assert_called_once_with(
        base_url=url,
        headers={header: "test", "User-Agent": f"pycoingecko/v{__version__}"},
    )
