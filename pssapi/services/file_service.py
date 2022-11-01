from typing import List as _List

from .raw import FileServiceRaw as _FileServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import File as _File
from ..entities import Sprite as _Sprite


class FileService(_ServiceBase):
    async def list_files(self, design_version: int = None) -> _List[_File]:
        result = await _FileServiceRaw.list_files_4(self.production_server, self.language_key, design_version)
        return result

    async def list_sprites(self, design_version: int = None) -> _List[_Sprite]:
        result = await _FileServiceRaw.list_sprites_2(self.production_server, self.language_key, design_version)
        return result
