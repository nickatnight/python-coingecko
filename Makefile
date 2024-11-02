all:

black:
	@echo "Running black"
	uv run black .

isort:
	@echo "Running isort"
	uv run isort .

ruff:
	@echo "Running ruff"
	uv run ruff check

mypy:
	@echo "Running mypy"
	uv run mypy .

lint-all: black isort ruff mypy

test:
	@echo "Running tests"
	uv run pytest --cov-report=html --cov=pycoingecko/ tests/
