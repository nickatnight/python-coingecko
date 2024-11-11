CoinGecko Demo Client
=====================

.. toctree::
    :maxdepth: 1
    :caption: Resources

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

APIs
----

.. code-block:: python

    from pycoingecko import CoinGecko

    client = CoinGecko()

    # PING
    client.ping.server_status()

    # SIMPLE
    client.simple.price_by_id(ids="bitcoin", vs_currencies="usd")

    client.simple.price_by_token_addresses(
        contract_addresses="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
        vs_currencies="usd"
    )

    client.simple.supported_currencies()

    # COINS
    client.coins.list_all()

    client.coins.list_with_markets(vs_currency="usd")

    client.coins.data_by_id(coin_id="bitcoin")

    client.coins.tickers_by_id(coin_id="bitcoin", vs_currency="usd")

    client.coins.historical_data_by_id(
        coin_id="bitcoin",
        date="30-12-2017",
        localization=False  # bool values get converted to strings before sending
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

    # CONTRACT
    client.contract.coin_data_by_token_address(
        coin_id="ethereum",
        contract_address="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"
    )

    client.contract.coin_historical_chart_by_token_address(
        coin_id="ethereum",
        contract_address="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
        vs_currency="usd",
        days="1"
    )

    client.contract.coin_historical_chart_range_by_token_address(
        coin_id="ethereum",
        contract_address="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
        vs_currency="usd",
        from_timestamp="1392577232",
        to_timestamp="1422577232"
    )

    # ASSET PLATFORMS
    client.asset_platforms.list_id_map()

    # CATEGORIES
    client.categories.categories_list()

    client.categories.categories_list_with_market_data(
        order="market_cap_desc",
    )

    # EXCHANGES
    client.exchanges.exchanges_list()

    client.exchanges.list_id_map()

    client.exchanges.by_id(
        exchange_id="binance"
    )

    client.exchanges.tickets_by_id(
        exchange_id="binance",
        coin_ids=["bitcoin", "ethereum"],  # can use a list here too, or comma separated string
    )

    client.exchanges.volume_chart_by_id(
        exchange_id="binance",
        days=1
    )
