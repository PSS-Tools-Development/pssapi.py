import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_challenge_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    challenge_designs = await client.challenge_service.list_all_challenge_designs(client_date_time)
    assert isinstance(challenge_designs, list)
    assert len(challenge_designs) > 0
    assert isinstance(challenge_designs[0], pssapi.entities.ChallengeDesign)
