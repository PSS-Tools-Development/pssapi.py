import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_division_designs(client: pssapi.PssApiClient):
    division_designs = await client.division_service.list_all_division_designs()
    assert isinstance(division_designs, list)
    assert len(division_designs) > 0
    assert isinstance(division_designs[0], pssapi.entities.DivisionDesign)
