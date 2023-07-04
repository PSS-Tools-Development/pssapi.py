import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_get_catalog_quantity(client: pssapi.PssApiClient):
    get_catalog_quantity = await client.live_ops_service.get_catalog_quantity()
    assert isinstance(get_catalog_quantity, pssapi.entities.GetCatalogQuantity)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_get_today_live_ops(client: pssapi.PssApiClient):
    live_ops = await client.live_ops_service.get_today_live_ops(pssapi.enums.DeviceType.ANDROID)
    assert isinstance(live_ops, pssapi.entities.LiveOps)
