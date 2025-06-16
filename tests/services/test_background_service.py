import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_backgrounds(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    backgrounds = await client.background_service.list_backgrounds(client_date_time)
    assert isinstance(backgrounds, list)
    assert len(backgrounds) > 0
    assert isinstance(backgrounds[0], pssapi.entities.Background)
