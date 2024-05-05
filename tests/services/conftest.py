import datetime
import os
import re

import pytest
import pytest_asyncio
import vcr.request

import pssapi

RX_ACCESS_TOKEN_IN_RESPONSE_BODY: re.Pattern = re.compile(r"accessToken=\".*?\"")
ACCESS_TOKEN_IN_RESPONSE_BODY_REPLACEMENT: str = 'accessToken="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"'


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
    return "99d2b3a5-75ff-469f-8dad-c57d558f4e8f"


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
        # "record_mode": "once",
        "record_mode": "rewrite",
        "filter_query_parameters": ["accessToken", "checksum"],
        "filter_post_data_parameters": ["accessToken", "checksum"],
        "record_on_exception": False,
        "before_record_request": before_record_request,
        "before_record_response": before_record_response,
    }


def before_record_request(request: vcr.request.Request):
    return request


def before_record_response(response):
    response_body = response["body"]["string"].decode("utf-8")
    if "accessToken" in response_body:
        response["body"]["string"] = (RX_ACCESS_TOKEN_IN_RESPONSE_BODY.sub(ACCESS_TOKEN_IN_RESPONSE_BODY_REPLACEMENT, response_body)).encode("utf-8")
    return response


@pytest.fixture(scope="module")
def vcr_cassette_dir(request: pytest.FixtureRequest):
    folder_name = request.module.__name__.split(".")[-1].removeprefix("test_")
    return f"tests/cassettes/{folder_name}"
