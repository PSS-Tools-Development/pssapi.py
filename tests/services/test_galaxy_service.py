import pytest

import pssapi

STAR_SYSTEM_ID: int = 53  # Golgotha


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client", "client_date_time")
@pytest.mark.vcr()
async def test_go_to(access_token: str, client: pssapi.PssApiClient, client_date_time_as_str: str):
    checksum = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ship = await client.galaxy_service.go_to(access_token, checksum, client_date_time_as_str, STAR_SYSTEM_ID)
    assert isinstance(ship, pssapi.entities.Ship)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_marker_generator_designs(client: pssapi.PssApiClient):
    marker_generator_designs = await client.galaxy_service.list_marker_generator_designs()
    assert isinstance(marker_generator_designs, list)
    assert len(marker_generator_designs) > 0
    assert isinstance(marker_generator_designs[0], pssapi.entities.StarSystemMarkerGenerator)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_planets(client: pssapi.PssApiClient):
    planets = await client.galaxy_service.list_planets()
    assert isinstance(planets, list)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_star_system_links(client: pssapi.PssApiClient):
    star_system_links = await client.galaxy_service.list_star_system_links()
    assert isinstance(star_system_links, list)
    assert len(star_system_links) > 0
    assert isinstance(star_system_links[0], pssapi.entities.StarSystemLink)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client", "client_date_time")
@pytest.mark.vcr()
async def test_list_star_system_markers(access_token: str, client: pssapi.PssApiClient, client_date_time_as_str: str):
    star_system_markers = await client.galaxy_service.list_star_system_markers(access_token, client_date_time_as_str)
    assert isinstance(star_system_markers, list)
    assert len(star_system_markers) > 0
    assert isinstance(star_system_markers[0], pssapi.entities.StarSystemMarker)


@pytest.mark.asyncio
@pytest.mark.usefixtures("access_token", "client")
@pytest.mark.vcr()
async def test_list_star_system_markers_and_user_markers(access_token: str, client: pssapi.PssApiClient):
    markers = await client.galaxy_service.list_star_system_markers_and_user_markers(access_token)
    assert isinstance(markers, tuple)
    assert len(markers) == 2
    for element in markers:
        assert isinstance(element, list)
    assert isinstance(markers[0][0], pssapi.entities.StarSystemMarker)
    assert isinstance(markers[1][0], pssapi.entities.UserMarker)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_star_systems(client: pssapi.PssApiClient):
    star_systems = await client.galaxy_service.list_star_systems()
    assert isinstance(star_systems, list)
    assert len(star_systems) > 0
    assert isinstance(star_systems[0], pssapi.entities.StarSystem)
