init:
	pip install -r requirements.txt

test:
	py.test tests

requirements:
	CUSTOM_COMPILE_COMMAND="make requirements" pip-compile requirements.in

build:
	python -m build

.PHONY: init test requirements build
