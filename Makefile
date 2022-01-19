.PHONY: all
all: format check test

.PHONY: init
init:
	pip install --upgrade pip
	pip install pip-tools
	pip-sync dev-requirements.txt

.PHONY: requirements
requirements:
	CUSTOM_COMPILE_COMMAND="make requirements" pip-compile --resolver=backtracking --output-file=requirements.txt pyproject.toml
	CUSTOM_COMPILE_COMMAND="make requirements" pip-compile --resolver=backtracking --extra dev,test --output-file=dev-requirements.txt pyproject.toml

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
