from unittest.mock import MagicMock

import pytest
import requests

from pycoingecko.utils.exceptions import CoinGeckoRequestError
from pycoingecko.utils.http import RequestsClient


def test_client_coingecko_request_error(mocker: MagicMock) -> None:
    # Arrange
    mocker.patch(
        "pycoingecko.utils.http.requests.get",
        side_effect=requests.exceptions.HTTPError("Error"),
    )

    # Act
    client = RequestsClient()

    # Assert
    with pytest.raises(CoinGeckoRequestError):
        client.send("fakeurl")


def test_client_coingecko_other_error(mocker: MagicMock) -> None:
    # Arrange
    mocker.patch(
        "pycoingecko.utils.http.requests.get",
        side_effect=ValueError("Error"),
    )

    # Act
    client = RequestsClient()

    # Assert
    with pytest.raises(ValueError):
        client.send("fakeurl")
