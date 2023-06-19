import pytest

from pssapi import PssApiClient


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_animations(client: PssApiClient):
    await client.animation_service.list_animations()
