from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import MessageRaw as _MessageRaw


class Message(_MessageRaw, _EntityWithIdBase):
    def __init__(self, message_info: _EntityInfo) -> None:
        super().__init__(message_info)

    @property
    def id(self) -> int:
        return self.message_id
