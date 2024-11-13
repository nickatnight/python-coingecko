CoinGecko Pro Client
====================
The pro client subclasses the demo client ``CoinGeckoDemoClient`` and has access to existing methods. The pro client contains additional methods only available to pro users. API docs can be found `here <https://docs.coingecko.com/reference/introduction>`_.

.. toctree::
    :maxdepth: 1
    :caption: Resources

    clients/pro/coins
    clients/pro/asset_platforms
    clients/pro/exchanges


APIs
----

.. code-block:: python

    from pycoingecko import CoinGecko

    client = CoinGecko(api_key="your-api-key", is_pro=True)

    # COINS

    # /api/v3/coins/top_gainers_losers
    client.coins.top_gainers_and_losers(vs_currency="usd", duration="1h", top_coins="300")

    # /v3/coins/list/new
    client.coins.recently_added()

    # /api/v3/coins/{id}/ohlc/range
    client.coins.ohlc_chart_within_time_range(
        coin_id="bitcoin",
        vs_currency="usd",
        from_timestamp=1636160000,
        to_timestamp=1636246400
    )

    # (enterprise plan)
    # /api/v3/coins/{id}/circulating_supply_chart
    client.coins.circulating_supply(
        coin_id="bitcoin",
        days="2",
    )

    # (enterprise plan)
    # /api/v3/coins/{id}/circulating_supply_chart/range
    client.coins.circulating_supply_within_time_range(
        coin_id="bitcoin",
        from_timestamp=1636160000,
        to_timestamp=1636246400
    )

    # (enterprise plan)
    # /api/v3/coins/{id}/total_supply_chart
    client.coins.total_supply(
        coin_id="bitcoin",
        days="2",
    )

    # (enterprise plan)
    # /api/v3/coins/{id}/total_supply_chart/range
    client.coins.total_supply_within_time_range(
        coin_id="bitcoin",
        from_timestamp=1636160000,
        to_timestamp=1636246400
    )

    # ASSET PLATFORMS

    # (enterprise plan)
    # /api/v3/token_lists/{asset_platform_id}/all.json
    client.asset_platforms.token_list(asset_platform_id='ethereum')

    # EXCHANGES

    # /api/v3/exchanges/{id}/volume_chart/range
    client.exchanges.volume_chart_within_time_range(
        exchange_id="binance",
        from_timestamp=1636160000,
        to_timestamp=1636246400
    )

    # NFTs (Beta)

    # /api/v3/nfts/markets
    client.nfts.collection_with_market_data()
