from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import FileRaw as _FileRaw


class File(_FileRaw, _EntityWithIdBase):
    def __init__(self, file_info: _EntityInfo) -> None:
        super().__init__(file_info)
        self._file_download_category_enum: _enums.FileDownloadCategory = _parse.pss_str_enum(self.file_download_category, _enums.FileDownloadCategory)

    @property
    def id(self) -> int:
        return self.id_

    @property
    def file_download_category_enum(self) -> "_enums.FileDownloadCategory":
        return self._file_download_category_enum
