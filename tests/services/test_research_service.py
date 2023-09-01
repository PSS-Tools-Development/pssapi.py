import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_research_designs(client: pssapi.PssApiClient):
    research_designs = await client.research_service.list_all_research_designs()
    assert isinstance(research_designs, list)
    assert len(research_designs) > 0
    assert isinstance(research_designs[0], pssapi.entities.ResearchDesign)
