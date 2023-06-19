import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_challenge_designs(client: pssapi.PssApiClient):
    challenge_designs = await client.challenge_service.list_all_challenge_designs()
    assert isinstance(challenge_designs, list)
    assert len(challenge_designs) > 0
    assert isinstance(challenge_designs[0], pssapi.entities.ChallengeDesign)
