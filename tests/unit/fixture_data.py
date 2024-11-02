class CoinGeckoAPIFixtureData:
    @classmethod
    def ping_response(cls) -> dict:
        return {"gecko_says": "(V3) To the Moon!"}

    @classmethod
    def simple_price_api_response(cls) -> dict:
        return {
            "bitcoin": {
                "usd": 67187.3358936566,
                "usd_market_cap": 1317802988326.25,
                "usd_24h_vol": 31260929299.5248,
                "usd_24h_change": 3.63727894677354,
                "last_updated_at": 1711356300,
            }
        }

    @classmethod
    def simple_token_price_api_response(cls) -> dict:
        return {
            "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599": {
                "usd": 67187.3358936566,
                "usd_market_cap": 1317802988326.25,
                "usd_24h_vol": 31260929299.5248,
                "usd_24h_change": 3.63727894677354,
                "last_updated_at": 1711356300,
            }
        }

    @classmethod
    def asset_platforms_response(cls) -> list:
        return [
            {
                "id": "polygon-pos",
                "chain_identifier": 137,
                "name": "Polygon POS",
                "shortname": "MATIC",
                "native_coin_id": "matic-network",
                "image": {
                    "thumb": "https://coin-images.coingecko.com/asset_platforms/images/15/thumb/polygon_pos.png?1706606645",
                    "small": "https://coin-images.coingecko.com/asset_platforms/images/15/small/polygon_pos.png?1706606645",
                    "large": "https://coin-images.coingecko.com/asset_platforms/images/15/large/polygon_pos.png?1706606645",
                },
            }
        ]

    @classmethod
    def categories_response(cls) -> list:
        return [
            {"category_id": "aave-tokens", "name": "Aave Tokens"},
            {"category_id": "aaccount-abstraction", "name": "Account Abstraction"},
        ]

    @classmethod
    def categories_with_market_data_response(cls) -> list:
        return [
            {
                "id": "layer-1",
                "name": "Layer 1 (L1)",
                "market_cap": 2061406861196.14,
                "market_cap_change_24h": -0.66091235190398,
                "content": "",
                "top_3_coins_id": ["bitcoin", "ethereum", "binancecoin"],
                "top_3_coins": [
                    "https://assets.coingecko.com/coins/images/1/small/bitcoin.png?1696501400",
                    "https://assets.coingecko.com/coins/images/279/small/ethereum.png?1696501628",
                    "https://assets.coingecko.com/coins/images/825/small/bnb-icon2_2x.png?1696501970",
                ],
                "volume_24h": 61146432400.1739,
                "updated_at": "2024-04-06T08:25:46.402Z",
            }
        ]

    @classmethod
    def coins_list_response(cls) -> list:
        return [
            {
                "id": "0chain",
                "symbol": "zcn",
                "name": "Zus",
                "platforms": {
                    "ethereum": "0xb9ef770b6a5e12e45983c5d80545258aa38f3b78",
                    "polygon-pos": "0x8bb30e0e67b11b978a5040144c410e1ccddcba30",
                },
            },
            {"id": "01coin", "symbol": "zoc", "name": "01coin", "platforms": {}},
        ]

    @classmethod
    def coins_markets_response(cls) -> list:
        return [
            {
                "id": "bitcoin",
                "symbol": "btc",
                "name": "Bitcoin",
                "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
                "current_price": 70187,
                "market_cap": 1381651251183,
                "market_cap_rank": 1,
                "fully_diluted_valuation": 1474623675796,
                "total_volume": 20154184933,
                "high_24h": 70215,
                "low_24h": 68060,
                "price_change_24h": 2126.88,
                "price_change_percentage_24h": 3.12502,
                "market_cap_change_24h": 44287678051,
                "market_cap_change_percentage_24h": 3.31157,
                "circulating_supply": 19675987,
                "total_supply": 21000000,
                "max_supply": 21000000,
                "ath": 73738,
                "ath_change_percentage": -4.77063,
                "ath_date": "2024-03-14T07:10:36.635Z",
                "atl": 67.81,
                "atl_change_percentage": 103455.83335,
                "atl_date": "2013-07-06T00:00:00.000Z",
                "roi": None,
                "last_updated": "2024-04-07T16:49:31.736Z",
            }
        ]

    @classmethod
    def coin_by_id_response(cls) -> dict:
        return {}

    @classmethod
    def coin_tickers_by_id_response(cls) -> dict:
        return {
            "name": "Bitcoin",
            "tickers": [
                {
                    "base": "BTC",
                    "target": "USDT",
                    "market": {
                        "name": "Binance",
                        "identifier": "binance",
                        "has_trading_incentive": False,
                        "logo": "https://assets.coingecko.com/markets/images/52/small/binance.jpg?1706864274",
                    },
                    "last": 69476,
                    "volume": 20242.03975,
                    "cost_to_move_up_usd": 19320706.3958517,
                    "cost_to_move_down_usd": 16360235.3694131,
                    "converted_last": {"btc": 1.000205, "eth": 20.291404, "usd": 69498},
                    "converted_volume": {
                        "btc": 20249,
                        "eth": 410802,
                        "usd": 1406996874,
                    },
                    "trust_score": "green",
                    "bid_ask_spread_percentage": 0.010014,
                    "timestamp": "2024-04-08T04:02:01+00:00",
                    "last_traded_at": "2024-04-08T04:02:01+00:00",
                    "last_fetch_at": "2024-04-08T04:03:00+00:00",
                    "is_anomaly": False,
                    "is_stale": False,
                    "trade_url": "https://www.binance.com/en/trade/BTC_USDT?ref=37754157",
                    "token_info_url": None,
                    "coin_id": "bitcoin",
                    "target_coin_id": "tether",
                }
            ],
        }

    @classmethod
    def coin_history_by_id_response(cls) -> dict:
        return {
            "prices": [
                [1711843200000, 69702.3087473573],
                [1711929600000, 71246.9514406015],
                [1711983682000, 68887.7495158568],
            ],
            "market_caps": [
                [1711843200000, 1370247487960.09],
                [1711929600000, 1401370211582.37],
                [1711983682000, 1355701979725.16],
            ],
            "total_volumes": [
                [1711843200000, 16408802301.8374],
                [1711929600000, 19723005998.215],
                [1711983682000, 30137418199.6431],
            ],
        }

    @classmethod
    def coin_ohlc_by_id_response(cls) -> list:
        return [
            [1709395200000, 61942, 62211, 61721, 61845],
            [1709409600000, 61828, 62139, 61726, 62139],
            [1709424000000, 62171, 62210, 61821, 62068],
        ]
