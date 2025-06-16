import datetime

import pytest

import pssapi


MISSION_DESIGN_ID: int = 244  # Explore Valhalla


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client", "client_date_time")
@pytest.mark.vcr(record_mode="once")
async def test_create_mission(client: pssapi.PssApiClient, access_token: str, client_date_time: datetime.datetime):
    checksum = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    mission = await client.mission_service.create_mission(access_token, checksum, client_date_time, 0, MISSION_DESIGN_ID)
    assert isinstance(mission, tuple)
    assert len(mission) == 4
    assert isinstance(mission[0], pssapi.entities.Battle)
    assert isinstance(mission[1], pssapi.entities.MissionEvent)
    assert isinstance(mission[2], pssapi.entities.User)
    assert isinstance(mission[3], list)
    assert len(mission[3]) > 0
    assert isinstance(mission[3][0], pssapi.entities.MissionEvent)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_mission_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    mission_designs = await client.mission_service.list_all_mission_designs(client_date_time)
    assert isinstance(mission_designs, list)
    assert len(mission_designs) > 0
    assert isinstance(mission_designs[0], pssapi.entities.MissionDesign)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client", "client_date_time")
@pytest.mark.vcr(record_mode="once")
async def test_select_event(client: pssapi.PssApiClient, access_token: str, client_date_time: datetime.datetime):
    checksum = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    event = await client.mission_service.select_event(access_token, 0, checksum, client_date_time, 0, 0)
    assert isinstance(event, tuple)
    assert len(event) == 2
    assert isinstance(event[0], pssapi.entities.Battle)
    assert isinstance(event[1], pssapi.entities.User)
