from typing import List as _List
from typing import Tuple as _Tuple

from .raw import FileServiceRaw as _FileServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import File as _File
from ..entities import Sprite as _Sprite


class FileService(_ServiceBase):
    async def list_files(self, design_version: int = None) -> _List[_File]:
        production_server = await self.get_production_server()
        result = await _FileServiceRaw.list_files_4(production_server, design_version, self.language_key)
        return result

    async def list_sprites(self, design_version: int = None) -> _List[_Sprite]:
        production_server = await self.get_production_server()
        result = await _FileServiceRaw.list_sprites_2(production_server, design_version, self.language_key)
        return result

