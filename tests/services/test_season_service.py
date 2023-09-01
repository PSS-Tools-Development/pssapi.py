import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_season_designs(client: pssapi.PssApiClient):
    season_designs = await client.season_service.list_all_season_designs()
    assert isinstance(season_designs, list)
    assert len(season_designs) > 0
    assert isinstance(season_designs[0], pssapi.entities.SeasonDesign)
