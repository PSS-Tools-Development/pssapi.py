import pytest

from pssapi import PssApiClient


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_challenge_designs(client: PssApiClient):
    await client.challenge_service.list_all_challenge_designs()
