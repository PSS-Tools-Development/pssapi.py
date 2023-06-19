import os

import pytest

import pssapi


@pytest.fixture(scope="session")
def client() -> pssapi.PssApiClient:
    client = pssapi.PssApiClient(device_type=pssapi.enums.DeviceType.ANDROID, language_key=pssapi.enums.LanguageKey.ENGLISH, production_server="api.pixelstarships.com")
    return client


@pytest.fixture(scope="session")
def access_token() -> str:
    return os.environ.get("PSS_ACCESS_TOKEN")


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "match_on": ["host", "method", "path", "scheme"],
        "record_mode": "once",
    }


@pytest.fixture(scope="function")
def vcr_cassette_name(request):
    cassette_name = request.node.name.removeprefix("test_")
    return cassette_name


@pytest.fixture(scope="module")
def vcr_cassette_dir(request):
    folder_name = request.module.__name__.split(".")[-1].removeprefix("test_")
    return f"tests/cassettes/{folder_name}"
