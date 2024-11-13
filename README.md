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
        <img alt="Python Versions Shield" src="https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white">
    </a>
    <a href="https://python-coingecko.readthedocs.io/en/stable/"><img alt="Read The Docs Badge" src="https://img.shields.io/readthedocs/python-coingecko"></a>
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

## Documentation
See full documentation [here](https://python-coingecko.readthedocs.io/en/latest/).
