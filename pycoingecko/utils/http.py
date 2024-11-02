import copy
import logging
from typing import Any, Optional

import requests

from pycoingecko.utils.exceptions import CoinGeckoRequestError
from pycoingecko.utils.interfaces import IHttp


logger = logging.getLogger(__name__)
default_headers = {"Content-Type": "application/json"}


class RequestsClient(IHttp):
    def __init__(
        self, base_url: Optional[str] = "", headers: Optional[dict] = None
    ) -> None:
        self.base_url = base_url
        self.headers = copy.deepcopy(default_headers)

        if headers is not None:
            self.headers.update(**headers)

    def send(self, path: str, method: str = "get", **extra: Any) -> dict | list:
        url = f"{self.base_url}{path}"
        headers = extra.pop("headers", {})

        self.headers.update(**headers)

        req_to_call = getattr(requests, method.lower())

        try:
            response = req_to_call(url, headers=self.headers, **extra)
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
