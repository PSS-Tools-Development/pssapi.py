import datetime

import pytest

import pssapi

MISSILE_DESIGN_ID: int = 2  # Rocket Lv1
ROOM_DESIGN_ID: int = 2  # Bedroom Lv1


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_get_missile_design(client: pssapi.PssApiClient):
    missile_design = await client.room_service.get_missile_design(MISSILE_DESIGN_ID)
    assert isinstance(missile_design, pssapi.entities.MissileDesign)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_get_room_design(client: pssapi.PssApiClient):
    room_design = await client.room_service.get_room_design(ROOM_DESIGN_ID)
    assert isinstance(room_design, pssapi.entities.RoomDesign)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_action_types(client: pssapi.PssApiClient):
    action_types = await client.room_service.list_action_types()
    assert isinstance(action_types, list)
    assert len(action_types) > 0
    assert isinstance(action_types[0], pssapi.entities.ActionType)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_condition_types(client: pssapi.PssApiClient):
    condition_types = await client.room_service.list_condition_types()
    assert isinstance(condition_types, list)
    assert len(condition_types) > 0
    assert isinstance(condition_types[0], pssapi.entities.ConditionType)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_craft_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    craft_designs = await client.room_service.list_craft_designs(client_date_time)
    assert isinstance(craft_designs, list)
    assert len(craft_designs) > 0
    assert isinstance(craft_designs[0], pssapi.entities.CraftDesign)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_missile_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    missile_designs = await client.room_service.list_missile_designs(client_date_time)
    assert isinstance(missile_designs, list)
    assert len(missile_designs) > 0
    assert isinstance(missile_designs[0], pssapi.entities.MissileDesign)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_room_design_purchase(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    room_design_purchases = await client.room_service.list_room_design_purchase(client_date_time)
    assert isinstance(room_design_purchases, list)
    assert len(room_design_purchases) > 0
    assert isinstance(room_design_purchases[0], pssapi.entities.RoomDesignPurchase)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_room_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    room_designs = await client.room_service.list_room_designs(client_date_time)
    assert isinstance(room_designs, list)
    assert len(room_designs) > 0
    assert isinstance(room_designs[0], pssapi.entities.RoomDesign)
