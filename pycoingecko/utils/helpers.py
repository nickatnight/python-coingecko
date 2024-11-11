import functools
from typing import Any, Callable


def get_client_api_methods(client: object) -> list:
    return [
        member
        for member in dir(client)
        if not member.startswith("__") and member != "http"
    ]


def as_gecko_args(func: Callable) -> Callable:
    """decorator to convert arguments to format expected by CoinGecko API

    boolean values are converted to lowercase strings
    list values are converted to comma-separated strings
    """

    @functools.wraps(func)
    def wrapper_as_gecko_args(*args: int, **kwargs: Any) -> Any:
        # check in **kwargs for lists and booleans
        for kwarg in kwargs:
            value = kwargs[kwarg]

            # check if arg is list and convert it to comma-separated string
            if isinstance(value, list):
                value = ",".join(value)
            # check if arg is boolean and convert it to string
            elif isinstance(value, bool):
                value = str(value).lower()

            kwargs[kwarg] = value

        return func(*args, **kwargs)

    return wrapper_as_gecko_args
