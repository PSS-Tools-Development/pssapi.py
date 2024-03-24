import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_all_reward_designs(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    reward_designs = await client.reward_service.list_all_reward_designs(client_date_time)
    assert isinstance(reward_designs, list)
    assert len(reward_designs) > 0
    assert isinstance(reward_designs[0], pssapi.entities.RewardDesign)
