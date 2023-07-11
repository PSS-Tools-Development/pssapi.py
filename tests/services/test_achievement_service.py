import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_achievement_designs(client: pssapi.PssApiClient):
    achievement_designs = await client.achievement_service.list_achievement_designs()
    assert isinstance(achievement_designs, list)
    assert len(achievement_designs) > 0
    assert isinstance(achievement_designs[0], pssapi.entities.AchievementDesign)
