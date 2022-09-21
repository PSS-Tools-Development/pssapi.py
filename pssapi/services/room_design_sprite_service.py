from typing import List as _List

from .raw import RoomDesignSpriteServiceRaw as _RoomDesignSpriteServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import RoomDesignSprite as _RoomDesignSprite


class RoomDesignSpriteService(_ServiceBase, _RoomDesignSpriteServiceRaw):
    async def list_room_design_sprites(self, **params) -> _List[_RoomDesignSprite]:
        return self._list_room_design_sprites(self.production_server, **params)

    def __repr__(self) -> str:
        return f'<RoomDesignSpriteService: {self.name}>'

    def __str__(self) -> str:
        return f'<RoomDesignSpriteService: {self.name}>'
