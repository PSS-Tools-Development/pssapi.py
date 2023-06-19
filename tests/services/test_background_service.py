import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_backgrounds(client: pssapi.PssApiClient):
    await client.background_service.list_backgrounds()
