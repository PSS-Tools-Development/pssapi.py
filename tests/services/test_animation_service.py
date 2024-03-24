import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_animations(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    animations = await client.animation_service.list_animations(client_date_time)
    assert isinstance(animations, list)
    assert len(animations) > 0
    assert isinstance(animations[0], pssapi.entities.Animation)
