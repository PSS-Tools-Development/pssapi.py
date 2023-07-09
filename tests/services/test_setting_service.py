import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_get_latest_version(client: pssapi.PssApiClient):
    setting = await client.setting_service.get_settings(pssapi.enums.DeviceType.ANDROID)
    assert isinstance(setting, pssapi.entities.Setting)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_news_designs(client: pssapi.PssApiClient):
    news_designs = await client.setting_service.list_all_news_designs()
    assert isinstance(news_designs, list)
    assert len(news_designs) > 0
    assert isinstance(news_designs[0], pssapi.entities.NewsDesign)
