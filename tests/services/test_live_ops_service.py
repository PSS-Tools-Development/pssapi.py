import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_get_catalog_quantity(client: pssapi.PssApiClient):
    leagues = await client.live_ops_service.get_catalog_quantity()
    assert isinstance(leagues, pssapi.entities.GetCatalogQuantity)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_get_today_live_ops(client: pssapi.PssApiClient):
    leagues = await client.live_ops_service.get_today_live_ops(pssapi.enums.DeviceType.ANDROID)
    assert isinstance(leagues, pssapi.entities.LiveOps)
