from typing import List as _List

from .raw import RoomDesignSpriteServiceRaw as _RoomDesignSpriteServiceRaw
import pssapi.services.service_base as _service_base
from ..entities import RoomDesignSprite as _RoomDesignSprite


class RoomDesignSpriteService(_service_base.ServiceBase):
    async def list_room_design_sprites(self, design_version: int = None) -> _List[_RoomDesignSprite]:
        production_server = await self.get_production_server()
        result = await _RoomDesignSpriteServiceRaw.list_room_design_sprites(production_server, design_version)
        return result
