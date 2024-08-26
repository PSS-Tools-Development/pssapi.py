Set-StrictMode -Version Latest

function all {
    format
    check
    coverage
}

function init-dev {
	uv self update
	uv python install
	uv sync
	uv run pre-commit install
	uv run pre-commit run --all-files
}

function format {
    & uv run autoflake .
    & uv run isort .
    & uv run black .
}

function check {
    & uv run flake8 .
}

function test {
    uv run pytest
}

function coverage {
    uv run pytest --cov=./src/pssapi --cov-report=xml:cov.xml --cov-report=term
}

function build {
	rm -rf dist/*
	uvx --from build pyproject-build --installer uv
}

function publish {
	uv pip install -U twine
	make build
	twine check dist/*
	twine upload --repository pssapi.py dist/*
}

$target = $args[0]

switch ($target) {
    "all" {
        all

        break
    }

    "init-dev" {
        init-dev

        break
    }

    "format" {
        format

        break
    }

    "check" {
        check

        break
    }

    "test" {
        test

        break
    }

    "coverage" {
        coverage

        break
    }

    "build" {
        build

        break
    }

    "publish" {
        publish

        break
    }

    default {
        "Valid keywords: all, build, check, coverage, format, init-dev, publish, test"

        break
    }
}
