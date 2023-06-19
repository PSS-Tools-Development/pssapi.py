import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_challenge_designs(client: pssapi.PssApiClient):
    await client.challenge_service.list_all_challenge_designs()
