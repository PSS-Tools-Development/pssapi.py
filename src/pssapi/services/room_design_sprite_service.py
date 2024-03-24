import datetime as _datetime
from typing import List as _List

import pssapi.services.service_base as _service_base

from .. import utils as _utils
from ..entities import RoomDesignSprite as _RoomDesignSprite
from .raw import RoomDesignSpriteServiceRaw as _RoomDesignSpriteServiceRaw


class RoomDesignSpriteService(_service_base.CacheableServiceBase):
    async def list_room_design_sprites(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_RoomDesignSprite]:
        production_server = await self.get_production_server()
        result = await _RoomDesignSpriteServiceRaw.list_room_design_sprites_2(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version, self.language_key)
        return result
