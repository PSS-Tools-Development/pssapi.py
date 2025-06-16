import datetime

import pytest

import pssapi


CHARACTER_DESIGN_ID: int = 19  # Xin


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_character_design_actions(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    character_design_actions = await client.character_service.list_all_character_design_actions(client_date_time)
    assert isinstance(character_design_actions, list)
    assert len(character_design_actions) > 0
    assert isinstance(character_design_actions[0], pssapi.entities.CharacterDesignAction)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_character_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    character_designs = await client.character_service.list_all_character_designs(client_date_time)
    assert isinstance(character_designs, list)
    assert len(character_designs) > 0
    assert isinstance(character_designs[0], pssapi.entities.CharacterDesign)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_character_design_character_parts(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    character_designs = await client.character_service.list_all_character_designs(client_date_time)
    character_design = character_designs[0]
    character_parts = character_design.character_parts

    assert isinstance(character_parts, list)
    assert len(character_parts) > 0
    assert isinstance(character_parts[0], pssapi.entities.CharacterPart)
    assert character_parts[0].character_part_type == "Head"


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_draw_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    draw_designs = await client.character_service.list_all_draw_designs(client_date_time)
    assert isinstance(draw_designs, list)
    assert len(draw_designs) > 0
    assert isinstance(draw_designs[0], pssapi.entities.DrawDesign)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_prestige_character_to(client: pssapi.PssApiClient):
    prestiges = await client.character_service.prestige_character_to(CHARACTER_DESIGN_ID)
    assert isinstance(prestiges, list)
    assert len(prestiges) > 0
    assert isinstance(prestiges[0], pssapi.entities.Prestige)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_prestige_character_from(client: pssapi.PssApiClient):
    prestiges = await client.character_service.prestige_character_from(CHARACTER_DESIGN_ID)
    assert isinstance(prestiges, list)
    assert len(prestiges) > 0
    assert isinstance(prestiges[0], pssapi.entities.Prestige)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_to_character(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    character_designs = await client.character_service.to_character("Xin", client_date_time)
    assert isinstance(character_designs, list)
    assert len(character_designs) == 1
    assert isinstance(character_designs[0], pssapi.entities.CharacterDesign)
    assert character_designs[0].character_design_name == "Xin"
