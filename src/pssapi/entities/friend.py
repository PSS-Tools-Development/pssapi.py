from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import FriendRaw as _FriendRaw


class Friend(_FriendRaw, _EntityWithIdBase):
    def __init__(self, friend_info: _EntityInfo) -> None:
        super().__init__(friend_info)
        self._friend_type_enum: _enums.FriendType = _parse.pss_str_enum(self.friend_type, _enums.FriendType)

    @property
    def id(self) -> int:
        return self.id_

    @property
    def friend_type_enum(self) -> "_enums.FriendType":
        return self._friend_type_enum
