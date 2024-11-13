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

    # /api/v3/ping
    client.ping.server_status()

    # SIMPLE

    # /api/v3/simple/price
    client.simple.price_by_id(ids="bitcoin", vs_currencies="usd")

    # /api/v3/simple/token_price/{id}
    client.simple.price_by_token_addresses(
        contract_addresses="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
        vs_currencies="usd"
    )

    # /api/v3/simple/supported_vs_currencies
    client.simple.supported_currencies()

    # COINS

    # /api/v3/coins/list
    client.coins.list_all()

    # /api/v3/coins/markets
    client.coins.list_with_markets(vs_currency="usd")

    # /api/v3/coins/{id}
    client.coins.data_by_id(coin_id="bitcoin")

    # /api/v3/coins/{id}/tickers
    client.coins.tickers_by_id(coin_id="bitcoin", vs_currency="usd")

    # /api/v3/coins/{id}/history
    client.coins.historical_data_by_id(
        coin_id="bitcoin",
        date="30-12-2017",
        localization=False  # bool values get converted to strings before sending
    )

    # /api/v3/coins/{id}/market_chart
    client.coins.historical_chart_data_by_id(
        coin_id="bitcoin",
        vs_currency="usd",
        days="1",
        interval="hourly"
    )

    # /api/v3/coins/{id}/market_chart/range
    client.coins.historical_chart_data_within_time_range_by_id(
        coin_id="bitcoin",
        vs_currency="usd",
        from_timestamp="1392577232",
        to_timestamp="1422577232"
    )

    # /api/v3/coins/{id}/ohlc
    client.coins.ohlc_chart_by_id(
        coin_id="bitcoin",
        vs_currency="usd",
        days="1"
    )

    # CONTRACT

    # /v3/coins/{id}/contract/{contract_address}
    client.contract.coin_data_by_token_address(
        coin_id="ethereum",
        contract_address="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"
    )

    # /api/v3/coins/{id}/contract/{contract_address}/market_chart
    client.contract.coin_historical_chart_by_token_address(
        coin_id="ethereum",
        contract_address="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
        vs_currency="usd",
        days="1"
    )

    # /api/v3/coins/{id}/contract/{contract_address}/market_chart/range
    client.contract.coin_historical_chart_range_by_token_address(
        coin_id="ethereum",
        contract_address="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
        vs_currency="usd",
        from_timestamp="1392577232",
        to_timestamp="1422577232"
    )

    # ASSET PLATFORMS

    # /api/v3/asset_platforms
    client.asset_platforms.list_id_map()

    # CATEGORIES

    # /api/v3/coins/categories/list
    client.categories.categories_list()

    # /api/v3/coins/categories
    client.categories.categories_list_with_market_data(
        order="market_cap_desc",
    )

    # EXCHANGES

    # /api/v3/exchanges
    client.exchanges.exchanges_list()

    # api/v3/exchanges/list
    client.exchanges.list_id_map()

    # /api/v3/exchanges/{id}
    client.exchanges.by_id(
        exchange_id="binance"
    )

    # /api/v3/exchanges/{id}/tickers
    client.exchanges.tickets_by_id(
        exchange_id="binance",
        coin_ids=["bitcoin", "ethereum"],  # can use a list here too, or comma separated string
    )

    # /api/v3/exchanges/{id}/volume_chart
    client.exchanges.volume_chart_by_id(
        exchange_id="binance",
        days=1
    )

    # DERIVATIVES

    # /api/v3/derivatives
    client.derivatives.ticker_list()

    # /api/v3/derivatives/exchanges
    client.derivatives.exchanges_list_with_data()

    # /api/v3/derivatives/exchanges/{id}
    client.derivatives.by_id(
        exchange_id="bitmex",
        include_tickers="all"
    )

    # /api/v3/derivatives/exchanges/list
    client.derivatives.list_id_map()

    # NFTs (Beta)
    
    # /api/v3/nfts/list
    client.nfts.nft_list()

    # /api/v3/nfts/{id}
    client.nfts.collection_by_id(collection_id="pudgy-penguins")

    # /api/v3/nfts/{asset_platform_id}/contract/{contract_address}
    client.nfts.collection_by_contract_address(asset_platform_id="ethereum", contract_address="0x06012c8cf97bead5deae237070f9587f8e7a266d")

    # EXCHANGE RATES
    
    # api/v3/exchange_rates
    client.exchange_rates.btc_to_currency()

    # SEARCH

    # /api/v3/search
    client.search.query(q="sol")

    # TRENDING

    # /api/v3/search/trending
    client.trending.search()

    # GLOBAL

    # /api/v3/global
    client.global_data.crypto_market_data()

    # /api/v3/global/decentralized_finance_defi
    client.global_data.defi_market_data()

    # COMPANIES (Beta)

    # /api/v3/companies/public_treasury/{coin_id}
    client.companies.holdings(coin_id="bitcoin")
