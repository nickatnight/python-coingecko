Quick Start
===========

CoinGecko.com API supports to two versions, the `demo <https://docs.coingecko.com/v3.0.1/reference/introduction>`_ and pro api. The demo api is free and contains a subset of routes compared to the pro.
To use the CoinGecko demo client, simply initialize the ``CoinGecko`` client with no arguments:

.. code-block:: python

    from pycoingecko import CoinGecko

    client = CoinGecko()

    client.simple.price_by_id(ids="bitcoin", vs_currencies="usd")

Or you can use the pro client by passing in your api key and a boolean to indicate you want access to pro api:

.. code-block:: python

    from pycoingecko import CoinGecko

    client = CoinGecko(api_key="your-api-key", is_pro=True)

    client.coins.circulating_supply(coin_id="bitcoin")

Rate Limits
-----------

CoinGecko’s Public API has a rate limit of 5 to 15 calls per minute, depending on usage conditions worldwide. Demo accounts have a stable rate limit of 30 calls per minute.

There is a retry strategy implemented in the http client to handle rate limits. If you exceed the rate limit, the client will retry a total of 3 times with a back-off factor delay of 2.

.. code-block:: python

    for i in range(10):
        client.ping.server_status()

    2024-11-06 22:33:21,731 [DEBUG] https://api.coingecko.com:443 "GET /api/v3/ping HTTP/11" 200 None
    {'gecko_says': '(V3) To the Moon!'}
    2024-11-06 22:33:21,844 [DEBUG] https://api.coingecko.com:443 "GET /api/v3/ping HTTP/11" 200 None
    {'gecko_says': '(V3) To the Moon!'}
    2024-11-06 22:33:21,965 [DEBUG] https://api.coingecko.com:443 "GET /api/v3/ping HTTP/11" 200 None
    {'gecko_says': '(V3) To the Moon!'}
    2024-11-06 22:33:21,991 [DEBUG] https://api.coingecko.com:443 "GET /api/v3/ping HTTP/11" 429 187
    2024-11-06 22:33:21,992 [DEBUG] Incremented Retry for (url='/api/v3/ping'): Retry(total=2, connect=None, read=None, redirect=None, status=None)
    2024-11-06 22:34:21,997 [DEBUG] Retry: /api/v3/ping
    2024-11-06 22:34:22,162 [DEBUG] https://api.coingecko.com:443 "GET /api/v3/ping HTTP/11" 200 None
    ...