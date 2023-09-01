import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_task_designs(client: pssapi.PssApiClient):
    task_designs = await client.task_service.list_all_task_designs()
    assert isinstance(task_designs, list)
    assert len(task_designs) > 0
    assert isinstance(task_designs[0], pssapi.entities.TaskDesign)
