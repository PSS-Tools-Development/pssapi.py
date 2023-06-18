import pytest

from pssapi import PssApiClient, enums


@pytest.fixture(scope="session")  # one server to rule'em all
def client() -> PssApiClient:
    client = PssApiClient(device_type=enums.DeviceType.ANDROID, language_key=enums.LanguageKey.ENGLISH, production_server="api.pixelstarships.com")
    return client
