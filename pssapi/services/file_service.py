from typing import List as _List

from .raw import FileServiceRaw as _FileServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import File as _File
from ..entities import Sprite as _Sprite


class FileService(_ServiceBase, _FileServiceRaw):
    async def list_files_4(self, design_version: int = None, **params) -> _List[_File]:
        return await self._list_files_4(self.production_server, self.language_key, design_version, **params)

    async def list_sprites_2(self, design_version: int = None, **params) -> _List[_Sprite]:
        return await self._list_sprites_2(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<FileService: {self.name}>'

    def __str__(self) -> str:
        return f'<FileService: {self.name}>'
