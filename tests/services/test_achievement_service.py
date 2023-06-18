import pytest
import vcr

from pssapi import PssApiClient


@vcr.use_cassette("tests/cassettes/list_achievement_designs.yaml")
@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
async def test_list_achievement_designs(client: PssApiClient):
    await client.achievement_service.list_achievement_designs()
