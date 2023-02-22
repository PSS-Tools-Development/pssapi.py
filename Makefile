init:
	pip install --upgrade pi
	pip install pip-tools
	pip-sync

test:
	py.test tests

requirements:
	CUSTOM_COMPILE_COMMAND="make requirements" pip-compile --resolver=backtracking requirements.in

build:
	python -m build

.PHONY: init test requirements build
