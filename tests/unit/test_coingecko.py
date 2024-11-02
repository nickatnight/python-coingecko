import pytest

from pycoingecko.coingecko import CoinGecko
from pycoingecko.utils.exceptions import CoinGeckoClientError


def test_client_raises_error_on_invalid_input() -> None:
    # Arrange / Act / Assert
    with pytest.raises(CoinGeckoClientError):
        CoinGecko(api_key="test", is_pro=False, use_onchain=True)


def test_client_with_defaults() -> None:
    # Arrange
    client = CoinGecko(api_key="test")

    # Act / Assert
    assert client is not None
