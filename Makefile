.PHONY: all
all: format check test

.PHONY: init
init:
	poetry install

.PHONY: test
test:
	poetry run pytest

.PHONY: format
format:
	@poetry run autoflake .
	@poetry run isort .
	@poetry run black .

.PHONY: check
check:
	@poetry run flake8 .

.PHONY: build
build:
	poetry build
