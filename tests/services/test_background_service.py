import pytest

from pssapi import PssApiClient


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_backgrounds(client: PssApiClient):
    await client.background_service.list_backgrounds()
