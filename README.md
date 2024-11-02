# python-coingecko
<p align="center">
    <a href="https://github.com/nickatnight/python-coingecko/actions">
        <img alt="GitHub Actions status" src="https://github.com/nickatnight/python-coingecko/actions/workflows/main.yml/badge.svg">
    </a>
    <a href="https://codecov.io/gh/nickatnight/python-coingecko">
        <img alt="Coverage" src="https://codecov.io/gh/nickatnight/python-coingecko/branch/main/graph/badge.svg?token=I20H47UKRK"/>
    </a>
    <a href="https://github.com/nickatnight/python-coingecko/releases"><img alt="Release Status" src="https://img.shields.io/github/v/release/nickatnight/python-coingecko"></a>
    <a href="https://github.com/psf/black"><img alt="Style Badge" src="https://img.shields.io/badge/code%20style-black-000000"></a>
    <a href="https://github.com/nickatnight/python-coingecko/blob/master/LICENSE">
        <img alt="License Shield" src="https://img.shields.io/github/license/nickatnight/python-coingecko">
    </a>
</p>

⚠️ This package is actively being developed and accepting PRs (see TODO section)!

A Python wrapper for coingecko.com V3 api. Other notable api wrappers that didn't satisfy my need:
- [pycoingecko](https://github.com/man-c/pycoingecko) has not been active in over two years and does not support the newer endpoints

## Features
- ✏️ **MyPy** Fully typed using most [recent versions](https://mypy-lang.org/)
- ⚒️ **Modern tooling** like [uv](https://docs.astral.sh/uv/), [ruff](https://docs.astral.sh/ruff/), and [pre-commit](https://pre-commit.com/)
- 📥 **GitHub Actions** CI/CD to automate everything
- ↩️ **Code Coverage** Fully tested using tools like [Codecov](https://about.codecov.io/)

## Usage
For demo (free)
```
>>> from pycoingecko import CoinGecko
>>> coingecko = CoinGecko(api_key=<YOUR_API_KEY>)
>>> coingecko.simple.coin_price_by_id(ids="bitcoin")
{
  "bitcoin": {
    "usd": 67187.3358936566,
    "usd_market_cap": 1317802988326.25,
    "usd_24h_vol": 31260929299.5248,
    "usd_24h_change": 3.63727894677354,
    "last_updated_at": 1711356300
  }
}

```

Pro
```
>>> from pycoingecko import CoinGecko
>>> coingecko = CoinGecko(api_key=<YOUR_API_KEY>, is_pro=True)
>>> coingecko.coins.recently_added()
[
  {
    "id": "long-johnson",
    "symbol": "olong",
    "name": "Long Johnson",
    "activated_at": 1712562430
  },
  {
    "id": "dogita",
    "symbol": "doga",
    "name": "DOGITA",
    "activated_at": 1712562282
  },
  {
    "id": "bebe-on-base",
    "symbol": "bebe",
    "name": "Bebe on Base",
    "activated_at": 1712561709
  }
]
```
## TODO
### APIs

- Ping ✅
  - ~~Check API server status~~
- Simple ✅
  - ~~Coin Price~~
  - ~~Token Address Price~~
  - ~~Supported Currencies~~
- Coins ✅
  - ~~Coins List~~
  - ~~Coins List With Market Data~~
  - ~~Coin Data~~
  - ~~Coin Tickers~~
  - ~~Coin Historical Data~~
  - ~~Coin Historical Chart Data~~
  - ~~Coin Historical Chart Data Within Time Range~~
  - ~~Coin OHLC Chart~~
- Contract ✅
  - ~~Coin Data~~
  - ~~Coin Historical Chart Data~~
  - ~~Coin Historical Chart Data Within Time Range~~
- Asset Platforms ✅
  - ~~Asset List~~
- Categories ✅
  - ~~List Categories~~
  - ~~Market Data by Category~~
- Exchanges ✅
  - ~~List Exchanges~~
  - ~~Exchange Data~~
  - ~~Tickers~~
  - ~~Volume Chart~~
- Derivatives ✅
  - ~~Tickers~~
  - ~~Derivative Exchanges~~
  - ~~Derivative Data~~
- NFTs (Beta)
  - List NFTs
  - Collection Data
- Exchange Rates ✅
  - ~~BTC to Currency Rates~~
- Search ✅
  - ~~General Search~~
- Trending ✅
  - ~~Trending Search~~
- Global ✅
  - ~~Global Market Data~~
  - ~~DeFi Market Data~~
- Companies (Beta)
  - Public Companies Holdings
- ~~Pro~~
- Enterprise
- On Chain

### Ops
- ~~CI for coverage and codecov~~

### Docs
- ~~Update README~~
- Add sphinx

### Package
- Add polrs
- ~~100% coverage~~
