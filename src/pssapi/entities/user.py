from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserRaw as _UserRaw


class User(_UserRaw, _EntityWithIdBase):
    def __init__(self, user_info: _EntityInfo) -> None:
        super().__init__(user_info)

    @property
    def id(self) -> int:
        return self.id_
