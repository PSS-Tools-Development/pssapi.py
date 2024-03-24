import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_training_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    training_designs = await client.training_service.list_all_training_designs(client_date_time)
    assert isinstance(training_designs, list)
    assert len(training_designs) > 0
    assert isinstance(training_designs[0], pssapi.entities.TrainingDesign)
