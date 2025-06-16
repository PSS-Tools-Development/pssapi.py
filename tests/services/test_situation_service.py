import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_situation_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    situation_designs = await client.situation_service.list_situation_designs(client_date_time)
    assert isinstance(situation_designs, list)
    assert len(situation_designs) > 0
    assert isinstance(situation_designs[0], pssapi.entities.SituationDesign)
