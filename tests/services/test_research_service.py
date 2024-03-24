import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_research_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    research_designs = await client.research_service.list_all_research_designs(client_date_time)
    assert isinstance(research_designs, list)
    assert len(research_designs) > 0
    assert isinstance(research_designs[0], pssapi.entities.ResearchDesign)
