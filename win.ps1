Set-StrictMode -Version Latest

function all {
    format
    check
    coverage
}

function init-dev {
	rye self update
	rye sync --update-all
	pre-commit install
	pre-commit run --all-files
}

function format {
    & autoflake .
    & isort .
    & black .
}

function check {
    & flake8 .
}

function test {
    pytest
}

function coverage {
    pytest --cov=./src/pssapi --cov-report=xml:cov.xml --cov-report=term
}

function build {
    rye build --clean
}

function publish {
    rye build --clean
	rye publish --yes
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
