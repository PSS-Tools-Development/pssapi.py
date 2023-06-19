import pytest
import vcr

from pssapi import PssApiClient

ALLIANCE_ID = 21  # Trek Wolfpack
ALLIANCE_NAME = "Trek Wolfpack"


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_get_alliance(access_token: str, client: PssApiClient):
    await client.alliance_service.get_alliance(access_token, ALLIANCE_ID)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_list_alliances_by_championship_score_ranking(access_token: str, client: PssApiClient):
    await client.alliance_service.list_alliances_by_championship_score_ranking(access_token, 0, 100)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_alliances_by_ranking(client: PssApiClient):
    await client.alliance_service.list_alliances_by_ranking(0, 100)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_alliances_with_division(client: PssApiClient):
    await client.alliance_service.list_alliances_with_division(None)
    await client.alliance_service.list_alliances_with_division(1)
    await client.alliance_service.list_alliances_with_division(2)
    await client.alliance_service.list_alliances_with_division(3)
    await client.alliance_service.list_alliances_with_division(4)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_list_characters_given_in_alliance(access_token: str, client: PssApiClient):
    await client.alliance_service.list_characters_given_in_alliance(access_token, ALLIANCE_ID, 0, 100)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_list_users(access_token: str, client: PssApiClient):
    await client.alliance_service.list_users(access_token, ALLIANCE_ID, 0, 100)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_search_alliances(access_token: str, client: PssApiClient):
    await client.alliance_service.search_alliances(access_token, ALLIANCE_NAME, 0, 100)
