init:
	pip install --upgrade pip
	pip install pip-tools
	pip-sync

test:
	pytest

lint:
	autoflake src/
	autopep8 src/

requirements:
	CUSTOM_COMPILE_COMMAND="make requirements" pip-compile --resolver=backtracking requirements.in

build:
	python -m build

.PHONY: init test requirements build
