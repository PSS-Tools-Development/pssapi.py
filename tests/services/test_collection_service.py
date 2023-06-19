import pytest

from pssapi import PssApiClient


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_collection_designs(client: PssApiClient):
    await client.collection_service.list_all_collection_designs()
