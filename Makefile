.PHONY: all
all: format check test

.PHONY: init
init:
	poetry install

.PHONY: test
test:
	pytest

.PHONY: format
format:
	@autoflake .
	@isort .
	@black .

.PHONY: check
check:
	@flake8 .

.PHONY: build
build:
	python -m build
