from typing import List

from pssapi.services import service_base

from ..entities import File, Sprite
from .raw import FileServiceRaw


class FileService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("FileVersion")
    async def list_files(self, design_version: int = None) -> List[File]:
        production_server = await self.get_production_server()
        result = await FileServiceRaw.list_files_4(production_server, design_version, self.language_key)
        return result

    @service_base.cache_endpoint("SpriteVersion")
    async def list_sprites(self, design_version: int = None) -> List[Sprite]:
        production_server = await self.get_production_server()
        result = await FileServiceRaw.list_sprites_2(production_server, design_version, self.language_key)
        return result
