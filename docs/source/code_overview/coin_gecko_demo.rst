CoinGecko Demo Client
=====================

.. toctree::
    :maxdepth: 1
    :caption: Clients

    clients/ping
    clients/simple
    clients/coins
    clients/contract
    clients/assets_platform
    clients/categories
    clients/exchanges
    clients/derivatives
    clients/nfts
    clients/exchange_rates
    clients/search
    clients/trending
    clients/global
    clients/companies

API Clients
-----------

.. code-block:: python

    from pycoingecko import CoinGecko

    client = CoinGecko()

    # Ping
    client.ping.server_status()

    # Simple
    client.simple.price_by_id(ids="bitcoin", vs_currencies="usd")

    client.simple.price_by_token_addresses(
        contract_addresses="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
        vs_currencies="usd"
    )

    client.simple.supported_currencies()

    # Coins
    client.coins.list_all()

    client.coins.list_with_markets(vs_currency="usd")

    client.coins.data_by_id(coin_id="bitcoin")

    client.coins.tickers_by_id(coin_id="bitcoin", vs_currency="usd")

    client.coins.historical_data_by_id(
        coin_id="bitcoin",
        date="30-12-2017",
        localization=False
    )

    client.coins.historical_chart_data_by_id(
        coin_id="bitcoin",
        vs_currency="usd",
        days="1",
        interval="hourly"
    )

    client.coins.historical_chart_data_within_time_range_by_id(
        coin_id="bitcoin",
        vs_currency="usd",
        from_timestamp="1392577232",
        to_timestamp="1422577232"
    )

    client.coins.ohlc_chart_by_id(
        coin_id="bitcoin",
        vs_currency="usd",
        days="1"
    )

    # Contract
