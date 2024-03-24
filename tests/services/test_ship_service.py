import datetime

import pytest

import pssapi

SHIP_DESIGN_NAME: str = "Oumaumau Progenitor Extended"
USER_ID: int = 4510693  # The worst.


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client", "client_date_time")
@pytest.mark.vcr(record_mode="once")
async def test_get_ship_by_user_id(access_token: str, client: pssapi.PssApiClient, client_date_time: str):
    ship = await client.ship_service.get_ship_by_user_id(access_token, client_date_time, USER_ID)
    assert isinstance(ship, pssapi.entities.Ship)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(record_mode="once")
async def test_inspect_ship(access_token: str, client: pssapi.PssApiClient):
    inspect_ship = await client.ship_service.inspect_ship(access_token, USER_ID)
    assert isinstance(inspect_ship, tuple)
    assert len(inspect_ship) == 2
    assert isinstance(inspect_ship[0], pssapi.entities.Ship)
    assert isinstance(inspect_ship[1], pssapi.entities.User)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_ship_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    ship_designs = await client.ship_service.list_all_ship_designs(client_date_time)
    assert isinstance(ship_designs, list)
    assert len(ship_designs) > 0
    assert isinstance(ship_designs[0], pssapi.entities.ShipDesign)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_to_ship(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    ship_designs = await client.ship_service.to_ship(SHIP_DESIGN_NAME, client_date_time)
    assert isinstance(ship_designs, list)
    assert len(ship_designs) == 1
    assert isinstance(ship_designs[0], pssapi.entities.ShipDesign)
    assert ship_designs[0].ship_design_name == SHIP_DESIGN_NAME
