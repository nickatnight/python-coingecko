class CoinGeckoApiUrls:
    # Ping
    PING = "ping"

    # Simple
    PRICE = "simple/price"
    TOKEN_PRICE = "simple/token_price/{id}"
    SUPPORTED_CURRENCIES = "simple/supported_vs_currencies"

    # Coins
    COINS_LIST = "coins/list"
    COINS_MARKETS = "coins/markets"
    COIN = "coins/{id}"
    COIN_TICKERS = "coins/{id}/tickers"
    COIN_HISTORY = "coins/{id}/history"
    COIN_HISTORY_CHART = "coins/{id}/market_chart"
    COIN_HISTORY_TIME_RANGE = "coins/{id}/market_chart/range"
    COIN_OHLC = "coins/{id}/ohlc"
    COIN_TOP_GAINERS_AND_LOSERS = "coins/top_gainers_losers"
    COIN_RECENTLY_ADDED = "coins/list/new"
    COIN_OHLC_CHART_TIME_RANGE = "coins/{id}/ohlc/range"
    COIN_CIRCULATING_SUPPLY = "coins/{coin_id}/circulating_supply_chart"
    COIN_CIRCULATING_SUPPLY_TIME_RANGE = "coins/{id}/circulating_supply_chart/range"
    COIN_TOTAL_SUPPLY = "coins/{id}/total_supply_chart"
    COIN_TOTAL_SUPPLY_TIME_RANGE = "coins/{id}/total_supply_chart/range"

    # Contract
    COINS_CONTRACT_ADDRESS = "coins/{id}/contract/{contract_address}"
    COINS_CONTRACT_CHART_ADDRESS_BY_TOKEN = (
        "coins/{id}/contract/{contract_address}/market_chart"
    )
    COINS_CONTRACT_CHART_RANGE_ADDRESS_BY_TOKEN = (
        "coins/{id}/contract/{contract_address}/market_chart/range"
    )

    # Asset platform
    ASSET_PLATFORMS = "asset_platforms"
    ASSET_PLATFORMS_TOKEN_LIST = "token_lists/{asset_platform_id}/all.json"

    # Categories
    CATEGORIES = "categories/list"
    CATEGORIES_MARKETS = "categories"

    # Exchanges
    EXCHANGES = "exchanges"
    EXCHANGES_LIST = "exchanges/list"
    EXCHANGE = "exchanges/{id}"
    EXCHANGE_TICKERS = "exchanges/{id}/tickers"
    EXCHANGE_VOLUME_CHART = "exchanges/{id}/volume_chart"
    EXCHANGE_VOLUME_CHART_TIME_RANGE = "exchanges/{id}/volume_chart/range"

    # Derivatives
    DERIVATIVES_TICKERS = "derivatives"
    DERIVATIVES_EXCHANGES = "derivatives/exchanges"
    DERIVATIVES_EXCHANGE = "derivatives/exchanges/{id}"
    DERIVATIVES_EXCHANGE_LIST = "derivatives/exchanges/list"

    # NFTs
    NFTS = "nfts/list"
    NFTS_COLLECTION = "nfts/{id}"
    NFTS_COLLECTION_CONTRACT_ADDRESS = (
        "nfts/{asset_platform_id}/contract/{contract_address}"
    )
    NFTS_MARKET = "nfts/markets"
    NFTS_HISTORICAL_CHART = "nfts/{id}/market_chart"
    NFTS_HISTORICAL_CHART_BY_ADDRESS = (
        "nfts/{asset_platform_id}/contract/{contract_address}/market_chart"
    )
    NFTS_TICKERS_BY_ID = "nfts/{id}/tickers"

    # BTC-to-currency exchange rates
    BTC_TO_CURRENCY = "exchange_rates"

    # Search
    SEARCH = "search"
    TRENDING = "search/trending"

    # Global
    GLOBAL = "global"
    GLOBAL_DEFI = "global/decentralized_finance_defi"
    GLOBAL_MARKET_CAP_CHART = "global/market_cap_chart"

    # Key
    KEY = "key"

    # Companies
    COMPANIES = "companies/public_treasury/{coin_id}"

    # On Chain
    ONCHAIN_TOKEN_PRICE_BY_ADDRESS = (
        "onchain/simple/networks/{network}/token_price/{addresses}"
    )
    ONCHAIN_NETWORKS = "onchain/networks"
    ONCHAIN_DEXES_BY_NETWORK = "onchain/networks/{network}/dexes"
    ONCHAIN_TRADES_BY_POOL_ADDRESS = (
        "onchain/networks/{network}/pools/{pool_address}/trades"
    )
    ONCHAIN_OHLCV_BY_POOL_ADDRESS = (
        "onchain/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}"
    )
    ONCHAIN_TRENDING_POOLS = "onchain/networks/trending_pools"
    ONCHAIN_POOLS_TRENDING_BY_NETWORK = "onchain/networks/{network}/trending_pools"
    ONCHAIN_POOL_BY_ADDRESS = "onchain/networks/{network}/pools/{address}"
    ONCHAIN_TOKENS_TOP_POOLS = "onchain/networks/{network}/tokens/{token_address}/pools"
