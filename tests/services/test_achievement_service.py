import pytest

from pssapi import PssApiClient


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
async def test_list_achievement_designs(client: PssApiClient):
    await client.achievement_service.list_achievement_designs()
