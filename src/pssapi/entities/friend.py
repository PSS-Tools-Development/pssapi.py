from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import FriendRaw as _FriendRaw


class Friend(_FriendRaw, _EntityWithIdBase):
    def __init__(self, friend_info: _EntityInfo) -> None:
        super().__init__(friend_info)

    @property
    def id(self) -> int:
        return self.id_
