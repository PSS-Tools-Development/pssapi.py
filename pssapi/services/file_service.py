from typing import List as _List

from .raw import FileServiceRaw as _FileServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import File as _File
from ..entities import Sprite as _Sprite


class FileService(_ServiceBase, _FileServiceRaw):
    async def list_files_4(self, **params) -> _List[_File]:
        return self._list_files_4(self.production_server, self.language_key, **params)

    async def list_sprites_2(self, **params) -> _List[_Sprite]:
        return self._list_sprites_2(self.production_server, self.language_key, **params)

    def __repr__(self) -> str:
        return f'<FileService: {self.name}>'

    def __str__(self) -> str:
        return f'<FileService: {self.name}>'
