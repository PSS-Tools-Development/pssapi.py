from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import RoomDesignSprite as _RoomDesignSprite
from .raw import RoomDesignSpriteServiceRaw as _RoomDesignSpriteServiceRaw


class RoomDesignSpriteService(_service_base.CacheableServiceBase):
    async def list_room_design_sprites(self, design_version: int = None) -> _List[_RoomDesignSprite]:
        production_server = await self.get_production_server()
        result = await _RoomDesignSpriteServiceRaw.list_room_design_sprites(production_server, design_version)
        return result
