.PHONY: all
all: format check coverage

# setup
.PHONY: init-dev
init-dev:
	uv self update
	uv python install
	uv sync
	uv run pre-commit install
	uv run pre-commit run --all-files

.PHONY: upgrade
upgrade:
	uv sync -U

# formatting and linting
.PHONY: check
check:
	uv run flake8 ./src
	uv run vulture

.PHONY: format
format:
	uv run autoflake .
	uv run isort .
	uv run black .

# testing
.PHONY: test
test:
	uv run pytest

.PHONY: coverage
coverage:
	uv run pytest --cov=./src/pssapi --cov-report=xml:cov.xml --cov-report=term

# build & publish
.PHONY: build
build:
	rm -rf dist/*
	uvx --from build pyproject-build --installer uv

.PHONY: publish
publish:
	uv pip install -U twine
	make build
	twine check dist/*
	twine upload --repository pssapi.py dist/*
