import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_animations(client: pssapi.PssApiClient):
    animations = await client.animation_service.list_animations()
    assert isinstance(animations, list)
    assert len(animations) > 0
    assert isinstance(animations[0], pssapi.entities.Animation)
