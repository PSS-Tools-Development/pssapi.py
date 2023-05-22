Set-StrictMode -Version Latest

function init {
    poetry install
}

function test {
    pytest
}

function format {
    & autoflake .
    & isort .
    & black .
}

function check {
    & flake8 .
}

function build {
    python -m build
}

function all {
    format
    check
    test
}

$target = $args[0]

switch ($target) {
    "init" {
        init

        break
    }

    "test" {
        test

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

    "build" {
        build

        break
    }

    "all" {
        all

        break
    }

    default {
        "Valid keywords: init, test, format, check, build, all"

        break
    }
}
