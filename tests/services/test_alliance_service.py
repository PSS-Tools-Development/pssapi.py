import pytest

import pssapi


ALLIANCE_ID = 21  # Trek Wolfpack
ALLIANCE_NAME = "Trek "


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(recode_mode="once")
async def test_get_alliance(access_token: str, client: pssapi.PssApiClient):
    alliance = await client.alliance_service.get_alliance(access_token, ALLIANCE_ID)
    assert isinstance(alliance, pssapi.entities.Alliance)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(recode_mode="once")
async def test_list_alliances_by_championship_score_ranking(access_token: str, client: pssapi.PssApiClient):
    alliances = await client.alliance_service.list_alliances_by_championship_score_ranking(access_token, 0, 100)
    assert isinstance(alliances, list)
    assert len(alliances) > 0
    assert isinstance(alliances[0], pssapi.entities.Alliance)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_alliances_by_ranking(client: pssapi.PssApiClient):
    alliances = await client.alliance_service.list_alliances_by_ranking(0, 100)
    assert isinstance(alliances, list)
    assert len(alliances) > 0
    assert isinstance(alliances[0], pssapi.entities.Alliance)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_alliances_with_division(client: pssapi.PssApiClient):
    results = []
    results.append(await client.alliance_service.list_alliances_with_division(None))
    results.append(await client.alliance_service.list_alliances_with_division(1))
    results.append(await client.alliance_service.list_alliances_with_division(2))
    results.append(await client.alliance_service.list_alliances_with_division(3))
    results.append(await client.alliance_service.list_alliances_with_division(4))

    for alliances in results:
        assert isinstance(alliances, list)
        # assert len(results) > 0   # Only true during tournament
        # assert isinstance(results[0], pssapi.entities.Alliance)   # Only true during tournament


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(recode_mode="once")
async def test_list_characters_given_in_alliance(access_token: str, client: pssapi.PssApiClient):
    characters = await client.alliance_service.list_characters_given_in_alliance(access_token, ALLIANCE_ID, 0, 100)
    assert isinstance(characters, list)
    assert len(characters) > 0
    assert isinstance(characters[0], pssapi.entities.Character)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(recode_mode="once")
async def test_list_users(access_token: str, client: pssapi.PssApiClient):
    users = await client.alliance_service.list_users(access_token, ALLIANCE_ID, 0, 100)
    assert isinstance(users, list)
    assert len(users) > 0
    assert isinstance(users[0], pssapi.entities.User)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(recode_mode="once")
async def test_search_alliances(access_token: str, client: pssapi.PssApiClient):
    alliances = await client.alliance_service.search_alliances(access_token, ALLIANCE_NAME, 0, 100)
    assert isinstance(alliances, list)
    assert len(alliances) > 0
    assert isinstance(alliances[0], pssapi.entities.Alliance)
