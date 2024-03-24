import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_season_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    season_designs = await client.season_service.list_all_season_designs(client_date_time)
    assert isinstance(season_designs, list)
    assert len(season_designs) > 0
    assert isinstance(season_designs[0], pssapi.entities.SeasonDesign)
