import datetime
import os

import pytest
import pytest_asyncio

import pssapi


@pytest.fixture(scope="session")
def access_token() -> str:
    return os.environ.get("PSS_ACCESS_TOKEN")


@pytest.fixture(scope="session")
def checksum_key() -> str:
    return os.environ.get("PSS_DEVICE_LOGIN_CHECKSUM_KEY")


@pytest.fixture(scope="session")
def client(device_type: pssapi.enums.DeviceType.ANDROID, language_key: str) -> pssapi.PssApiClient:
    return pssapi.PssApiClient(device_type=device_type, language_key=language_key, production_server="api.pixelstarships.com")


@pytest.fixture(scope="session")
def client_date_time() -> datetime.datetime:
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


@pytest_asyncio.fixture()
async def generated_access_token(client: pssapi.PssApiClient, device_key: str, device_type: pssapi.enums.DeviceType, client_date_time: datetime.datetime, checksum_key: str, language_key: str) -> str:
    checksum = client.user_service.utils.create_device_login_checksum(device_key, device_type, client_date_time, checksum_key)
    user_login = await client.user_service.device_login(checksum, client_date_time, device_key, device_type, language_key)
    result = user_login.access_token
    return result


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
def vcr_cassette_name(request: pytest.FixtureRequest):
    cassette_name = request.node.name.removeprefix("test_")
    return cassette_name


@pytest.fixture(scope="module")
def vcr_cassette_dir(request: pytest.FixtureRequest):
    folder_name = request.module.__name__.split(".")[-1].removeprefix("test_")
    return f"tests/cassettes/{folder_name}"
