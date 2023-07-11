import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_list_users_by_championship_score_ranking(client: pssapi.PssApiClient, access_token: str):
    users = await client.ladder_service.list_users_by_championship_score_ranking(access_token, 1, 100)
    assert isinstance(users, list)
    assert len(users) > 0
    assert isinstance(users[0], pssapi.entities.User)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_list_users_by_ranking(client: pssapi.PssApiClient, access_token: str):
    users = await client.ladder_service.list_users_by_ranking(access_token, 1, 100)
    assert isinstance(users, list)
    assert len(users) > 0
    assert isinstance(users[0], pssapi.entities.User)
