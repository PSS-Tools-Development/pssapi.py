init:
	pip install --upgrade pip
	pip install pip-tools
	pip-sync dev-requirements.txt

test:
	pytest

lint:
	autoflake src/
	autopep8 src/

requirements:
	CUSTOM_COMPILE_COMMAND="make requirements" pip-compile --resolver=backtracking --output-file=requirements.txt pyproject.toml
	CUSTOM_COMPILE_COMMAND="make requirements" pip-compile --resolver=backtracking --extra dev,test --output-file=dev-requirements.txt pyproject.toml

build:
	python -m build

.PHONY: init test requirements build
