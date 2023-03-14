from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import File as _File
from ..entities import Sprite as _Sprite
from .raw import FileServiceRaw as _FileServiceRaw


class FileService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("FileVersion")
    async def list_files(self, design_version: int = None) -> _List[_File]:
        production_server = await self.get_production_server()
        result = await _FileServiceRaw.list_files_4(production_server, design_version, self.language_key)
        return result

    @_service_base.cache_endpoint("SpriteVersion")
    async def list_sprites(self, design_version: int = None) -> _List[_Sprite]:
        production_server = await self.get_production_server()
        result = await _FileServiceRaw.list_sprites_2(production_server, design_version, self.language_key)
        return result
