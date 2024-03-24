import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_item_design_actions(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    item_design_actions = await client.item_service.list_item_design_actions(client_date_time)
    assert isinstance(item_design_actions, list)
    assert len(item_design_actions) > 0
    assert isinstance(item_design_actions[0], pssapi.entities.ItemDesignAction)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_item_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    item_designs = await client.item_service.list_item_designs(client_date_time)
    assert isinstance(item_designs, list)
    assert len(item_designs) > 0
    assert isinstance(item_designs[0], pssapi.entities.ItemDesign)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_to_item(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    item_designs = await client.item_service.to_item("Small Mineral Crate", client_date_time)
    assert isinstance(item_designs, list)
    assert len(item_designs) == 1
    assert isinstance(item_designs[0], pssapi.entities.ItemDesign)
    assert item_designs[0].item_design_name == "Small Mineral Crate"
