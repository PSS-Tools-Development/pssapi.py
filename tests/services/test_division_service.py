import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_division_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    division_designs = await client.division_service.list_all_division_designs(client_date_time)
    assert isinstance(division_designs, list)
    assert len(division_designs) > 0
    assert isinstance(division_designs[0], pssapi.entities.DivisionDesign)
