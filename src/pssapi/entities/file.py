from .entity_base import EntityWithIdBase
from .raw import FileRaw


class File(FileRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.id_


__all__ = [
    "File",
]
