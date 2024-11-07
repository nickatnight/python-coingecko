# python-coingecko
<p align="center">
    <a href="https://github.com/nickatnight/python-coingecko/actions">
        <img alt="GitHub Actions status" src="https://github.com/nickatnight/python-coingecko/actions/workflows/main.yml/badge.svg">
    </a>
    <a href="https://codecov.io/gh/nickatnight/python-coingecko">
        <img alt="Coverage" src="https://codecov.io/gh/nickatnight/python-coingecko/branch/main/graph/badge.svg?token=I20H47UKRK"/>
    </a>
    <a href="https://pypi.org/project/python-coingecko/">
        <img alt="PyPi Shield" src="https://img.shields.io/pypi/v/python-coingecko">
    </a>
    <a href="https://www.python.org/downloads/">
        <img alt="Python Versions Shield" src="https://img.shields.io/badge/Python-3.9%20|%203.10%20|%203.11%20|%203.12|%203.13%20-blue?logo=python&logoColor=white">
    </a>
    <a href="https://github.com/psf/black"><img alt="Style Badge" src="https://img.shields.io/badge/code%20style-black-000000"></a>
    <a href="https://github.com/nickatnight/python-coingecko/blob/master/LICENSE">
        <img alt="License Shield" src="https://img.shields.io/github/license/nickatnight/python-coingecko">
    </a>
</p>
A Python wrapper for coingecko.com V3 api. Other notable api wrappers that didn't satisfy my need:

- [pycoingecko](https://github.com/man-c/pycoingecko) has not been active in over two years and does not support the newer api endpoints

## Features
- 🪙 **CoinGecko** [api routes](https://docs.coingecko.com/reference/introduction), including current beta
- ♻️ **Retry Strategy** Sensible defaults to reliably retry/back-off fetching data from coingecko
- ✏️ **MyPy** Fully typed using most [recent versions](https://mypy-lang.org/)
- ⚒️ **Modern tooling** using [uv](https://docs.astral.sh/uv/), [ruff](https://docs.astral.sh/ruff/), and [pre-commit](https://pre-commit.com/)
- 📥 **GitHub Actions** CI/CD to automate [everything](.github/workflows/main.yml)
- ↩️ **Code Coverage** Fully tested using tools like [Codecov](https://about.codecov.io/)
- 🐍 **Python Support** All minor [versions](https://www.python.org/downloads/) from 3.9 are supported

## Installation
```sh
$ pip install python-coingecko
```

## Usage
Demo (free)
```
>>> from pycoingecko import CoinGecko
>>> coingecko = CoinGecko(api_key=<YOUR_API_KEY>)
>>> coingecko.simple.price_by_id(ids="bitcoin", include_24hr_vol=True)  # can use regular Python boolean...will get converted to string
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

On Chain (Pro)
```
>>> from pycoingecko import CoinGecko
>>> coingecko = CoinGecko(api_key=<YOUR_API_KEY>, is_pro=True)
>>> coingecko.onchain_pools.trending_list_by_network(network="eth", include="base_token")
{
  "data": [
    {
      "id": "eth_0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
      "type": "pool",
      "attributes": {
        "base_token_price_usd": "3653.12491645176",
        ...
      }
    ...
    }
  ]
}
```

## Development
To develop on this project, you'll need [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.

Install dev dependencies
```sh
$ uv sync
```

Run linters black/ruff/isort/mypy
```sh
$ make lint-all
```

Run pytest
```sh
$ make test
```
