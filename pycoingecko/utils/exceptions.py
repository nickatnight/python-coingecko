from requests import Response


class BaseCoinGeckoError(Exception):
    """Base class for exceptions in this module."""

    pass


class CoinGeckoRequestError(BaseCoinGeckoError):
    def __init__(self, message: str, response: Response) -> None:
        self.message = message

        super().__init__(message)

        self.response = response


class CoinGeckoClientError(BaseCoinGeckoError):
    pass
