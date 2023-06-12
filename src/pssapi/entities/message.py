from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import MessageRaw as _MessageRaw


class Message(_MessageRaw, _EntityWithIdBase):
    def __init__(self, message_info: _EntityInfo) -> None:
        super().__init__(message_info)
        self._activity_type_enum: _enums.ActivityType = _parse.pss_str_enum(self.activity_type, _enums.ActivityType)
        self._message_type_enum: _enums.MessageType = _parse.pss_str_enum(self.message_type, _enums.MessageType)

    @property
    def id(self) -> int:
        return self.message_id

    @property
    def activity_type_enum(self) -> "_enums.ActivityType":
        return self._activity_type_enum

    @property
    def message_type_enum(self) -> "_enums.MessageType":
        return self._message_type_enum
