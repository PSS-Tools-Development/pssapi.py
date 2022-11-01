
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import FileRaw as _FileRaw
from ..types import EntityInfo as _EntityInfo


class File(_EntityWithIdBase, _FileRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<File {self.id}>'

    def __str__(self) -> str:
        return f'<File {self.id}>'

    @property
    def id(self) -> int:
        return self.id
