import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_backgrounds(client: pssapi.PssApiClient):
    backgrounds = await client.background_service.list_backgrounds()
    assert isinstance(backgrounds, list)
    assert len(backgrounds) > 0
    assert isinstance(backgrounds[0], pssapi.entities.Background)
