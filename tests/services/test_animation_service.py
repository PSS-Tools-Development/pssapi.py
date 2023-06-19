import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_animations(client: pssapi.PssApiClient):
    await client.animation_service.list_animations()
