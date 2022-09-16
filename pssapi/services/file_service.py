from typing import List as _List

from .raw import FileServiceRaw as _FileServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import Sprite as _Sprite
from ...entities import File as _File


class FileService(_ServiceBase):
    async def list_files_4(self, language_key: str, design_version: int) -> _List[_File]:
        raise NotImplemented()
        result = await _FileServiceRaw.list_files_4(self.production_server, language_key: str, design_version: int)
        return result


    async def list_sprites_2(self, language_key: str, design_version: int) -> _List[_Sprite]:
        raise NotImplemented()
        result = await _FileServiceRaw.list_sprites_2(self.production_server, language_key: str, design_version: int)
        return result


