import os

import pytest

import pssapi


@pytest.fixture(scope="session")
def access_token() -> str:
    return os.environ.get("PSS_ACCESS_TOKEN")


@pytest.fixture(scope="session")
def checksum_key() -> str:
    return os.environ.get("PSS_DEVICE_LOGIN_CHECKSUM_KEY")


@pytest.fixture(scope="session")
def client() -> pssapi.PssApiClient:
    client = pssapi.PssApiClient(device_type=pssapi.enums.DeviceType.ANDROID, language_key=pssapi.enums.LanguageKey.ENGLISH, production_server="api.pixelstarships.com")
    return client


@pytest.fixture(scope="session")
def client_date_time() -> str:
    return pssapi.utils.get_utc_now()


@pytest.fixture(scope="session")
def client_date_time_as_str() -> str:
    return pssapi.utils.datetime.convert_to_pss_timestamp(client_date_time())


@pytest.fixture(scope="session")
def device_key() -> str:
    return "e6a3815568cd"


@pytest.fixture(scope="session")
def device_name() -> str:
    return "Samsung"


@pytest.fixture(scope="session")
def device_type() -> pssapi.enums.DeviceType:
    return pssapi.enums.DeviceType.ANDROID


@pytest.fixture(scope="session")
def language_key() -> pssapi.enums.LanguageKey:
    return pssapi.enums.LanguageKey.ENGLISH


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
