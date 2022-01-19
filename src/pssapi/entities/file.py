from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import FileRaw as _FileRaw


class File(_FileRaw, _EntityWithIdBase):
    def __init__(self, file_info: _EntityInfo) -> None:
        super().__init__(file_info)

    @property
    def id(self) -> int:
        return self.id_
