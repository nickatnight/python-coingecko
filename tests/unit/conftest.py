from typing import Any
from unittest.mock import MagicMock

import pytest

from pycoingecko.utils import RequestsClient


@pytest.fixture
def mock_requests_get(mocker: MagicMock) -> Any:
    return mocker.patch("requests.get")


@pytest.fixture
def mock_http_client() -> RequestsClient:
    return RequestsClient("mockapi")
