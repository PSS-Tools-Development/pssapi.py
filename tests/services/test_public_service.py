import pytest

import pssapi


USER_ID: int = 4510693  # The worst.


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(record_mode="once")
async def test_get_ship_details(client: pssapi.PssApiClient, access_token: str):
    ship = await client.public_service.get_ship_details(access_token, USER_ID)
    assert isinstance(ship, pssapi.entities.Ship)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr(record_mode="once")
async def test_get_ship_room_details(client: pssapi.PssApiClient, access_token: str):
    ship = await client.public_service.get_ship_room_details(access_token, USER_ID)
    assert isinstance(ship, pssapi.entities.Ship)
