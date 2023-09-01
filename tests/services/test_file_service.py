import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_files(client: pssapi.PssApiClient):
    division_designs = await client.file_service.list_files()
    assert isinstance(division_designs, list)
    assert len(division_designs) > 0
    assert isinstance(division_designs[0], pssapi.entities.File)


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_sprites(client: pssapi.PssApiClient):
    division_designs = await client.file_service.list_sprites()
    assert isinstance(division_designs, list)
    assert len(division_designs) > 0
    assert isinstance(division_designs[0], pssapi.entities.Sprite)
