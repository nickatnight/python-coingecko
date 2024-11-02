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
