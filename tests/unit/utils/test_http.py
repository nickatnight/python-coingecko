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


def test_client_success_response(mocker: MagicMock) -> None:
    # Arrange
    mock_response = MagicMock()
    mock_response.json = MagicMock(return_value={"data": "test"})
    mocker.patch(
        "pycoingecko.utils.http.requests.get",
        return_value=mock_response,
    )

    # Act
    client = RequestsClient()
    response = client.send("fakeurl")

    # Assert
    assert response == {"data": "test"}
    mock_response.json.assert_called_once()
    mock_response.raise_for_status.assert_called_once()
