from typing import List

from pssapi.services import service_base

from ..entities import RoomDesignSprite
from .raw import RoomDesignSpriteServiceRaw


class RoomDesignSpriteService(service_base.CacheableServiceBase):
    async def list_room_design_sprites(self, client_date_time: str, design_version: int = None) -> List[RoomDesignSprite]:
        production_server = await self.get_production_server()
        result = await RoomDesignSpriteServiceRaw.list_room_design_sprites_2(production_server, client_date_time, design_version, self.language_key)
        return result
