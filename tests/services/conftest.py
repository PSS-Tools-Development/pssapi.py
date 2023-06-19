import os

import pytest

from pssapi import PssApiClient, enums


@pytest.fixture(scope="session")
def client() -> PssApiClient:
    client = PssApiClient(device_type=enums.DeviceType.ANDROID, language_key=enums.LanguageKey.ENGLISH, production_server="api.pixelstarships.com")
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


@pytest.fixture(scope="module")
def vcr_cassette_dir(request):
    return "tests/cassettes/"