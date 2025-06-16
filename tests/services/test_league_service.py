import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_leagues(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    leagues = await client.league_service.list_leagues(None, client_date_time)
    assert isinstance(leagues, list)
    assert len(leagues) > 0
    assert isinstance(leagues[0], pssapi.entities.League)
