import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_leagues(client: pssapi.PssApiClient):
    leagues = await client.league_service.list_leagues(None)
    assert isinstance(leagues, list)
    assert len(leagues) > 0
    assert isinstance(leagues[0], pssapi.entities.League)
