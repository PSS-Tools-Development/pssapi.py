import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_collection_designs(client: pssapi.PssApiClient):
    collection_designs = await client.collection_service.list_all_collection_designs()
    assert isinstance(collection_designs, list)
    assert len(collection_designs) > 0
    assert isinstance(collection_designs[0], pssapi.entities.CollectionDesign)
