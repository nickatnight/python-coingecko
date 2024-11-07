import copy
import logging
from typing import Any, Optional

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from pycoingecko.utils.exceptions import CoinGeckoRequestError
from pycoingecko.utils.interfaces import IHttp


logger = logging.getLogger(__name__)
default_headers = {"Content-Type": "application/json"}


def _get_retry() -> Retry:
    return Retry(
        total=3,
        backoff_factor=2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"],
    )


class RequestsClient(IHttp):
    def __init__(
        self, base_url: Optional[str] = "", headers: Optional[dict] = None
    ) -> None:
        self.base_url = base_url
        _headers = copy.deepcopy(default_headers)

        if headers is not None:
            _headers.update(**headers)

        adapter = HTTPAdapter(max_retries=_get_retry())

        self.s = requests.Session()
        self.s.mount("https://", adapter)
        self.s.mount("http://", adapter)
        self.s.headers.update(_headers)

    def send(self, path: str, method: str = "get", **extra: Any) -> dict | list:
        url = f"{self.base_url}{path}"
        headers = extra.pop("headers", {})

        self.s.headers.update(headers)

        req_to_call = getattr(self.s, method.lower())

        try:
            response = req_to_call(url, **extra)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}", exc_info=True)
            raise CoinGeckoRequestError(
                message=str(http_err), response=http_err.response
            ) from None
        except Exception as err:
            logger.error(f"Other error occurred: {err}")
            raise

        return response.json()  # type: ignore
