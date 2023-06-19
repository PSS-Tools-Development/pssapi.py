import pytest

from pssapi import PssApiClient

CHARACTER_DESIGN_ID: int = 19  # Xin


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_character_design_actions(client: PssApiClient):
    await client.character_service.list_all_character_design_actions()


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_character_designs(client: PssApiClient):
    await client.character_service.list_all_character_designs()


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_draw_designs(client: PssApiClient):
    await client.character_service.list_all_draw_designs()


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_prestige_character_to(client: PssApiClient):
    await client.character_service.prestige_character_to(19)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_prestige_character_from(client: PssApiClient):
    await client.character_service.prestige_character_from(19)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_to_character(client: PssApiClient):
    await client.character_service.to_character("Xin")
