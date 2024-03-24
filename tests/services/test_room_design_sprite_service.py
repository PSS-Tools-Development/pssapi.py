import datetime

import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "client_date_time")
@pytest.mark.vcr()
async def test_list_room_design_sprites(client: pssapi.PssApiClient, client_date_time: datetime.datetime):
    room_design_sprites = await client.room_design_sprite_service.list_room_design_sprites(client_date_time)
    assert isinstance(room_design_sprites, list)
    assert len(room_design_sprites) > 0
    assert isinstance(room_design_sprites[0], pssapi.entities.RoomDesignSprite)
