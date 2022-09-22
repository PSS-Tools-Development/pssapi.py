from typing import List as _List

from .raw import RoomDesignSpriteServiceRaw as _RoomDesignSpriteServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import RoomDesignSprite as _RoomDesignSprite


class RoomDesignSpriteService(_ServiceBase, _RoomDesignSpriteServiceRaw):
    async def list_room_design_sprites(self, design_version: int = None, **params) -> _List[_RoomDesignSprite]:
        return await self._list_room_design_sprites(self.production_server, design_version, **params)

    def __repr__(self) -> str:
        return f'<RoomDesignSpriteService: {self.name}>'

    def __str__(self) -> str:
        return f'<RoomDesignSpriteService: {self.name}>'
