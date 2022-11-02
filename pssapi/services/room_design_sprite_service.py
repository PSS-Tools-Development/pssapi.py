from typing import List as _List

from .raw import RoomDesignSpriteServiceRaw as _RoomDesignSpriteServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import RoomDesignSprite as _RoomDesignSprite


class RoomDesignSpriteService(_ServiceBase):
    async def list_room_design_sprites(self, design_version: int = None) -> _List[_RoomDesignSprite]:
        result = await _RoomDesignSpriteServiceRaw.list_room_design_sprites(production_server=self.production_server, design_version=design_version)
        return result
