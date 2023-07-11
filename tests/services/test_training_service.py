import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_training_designs(client: pssapi.PssApiClient):
    training_designs = await client.training_service.list_all_training_designs()
    assert isinstance(training_designs, list)
    assert len(training_designs) > 0
    assert isinstance(training_designs[0], pssapi.entities.TrainingDesign)
