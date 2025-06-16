from datetime import datetime as _datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_task_designs(client: pssapi.PssApiClient, client_date_time: _datetime):
    task_designs = await client.task_service.list_all_task_designs(client_date_time)
    assert isinstance(task_designs, list)
    assert len(task_designs) > 0
    assert isinstance(task_designs[0], pssapi.entities.TaskDesign)
