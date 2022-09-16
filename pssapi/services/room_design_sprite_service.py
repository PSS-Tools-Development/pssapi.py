from typing import List as _List

from .raw import RoomDesignSpriteServiceRaw as _RoomDesignSpriteServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import RoomDesignSprite as _RoomDesignSprite


class RoomDesignSpriteService(_ServiceBase):
    async def list_room_design_sprites(self, design_version: int) -> _List[_RoomDesignSprite]:
        raise NotImplemented()
        result = await _RoomDesignSpriteServiceRaw.list_room_design_sprites(self.production_server, design_version: int)
        return result


