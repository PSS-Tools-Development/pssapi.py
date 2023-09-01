import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_situation_designs(client: pssapi.PssApiClient):
    situation_designs = await client.situation_service.list_situation_designs()
    assert isinstance(situation_designs, list)
    assert len(situation_designs) > 0
    assert isinstance(situation_designs[0], pssapi.entities.SituationDesign)
