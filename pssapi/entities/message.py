
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import MessageRaw as _MessageRaw
from ..types import EntityInfo as _EntityInfo


class Message(_EntityWithIdBase, _MessageRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<Message {self.id}>'

    def __str__(self) -> str:
        return f'<Message {self.id}>'

    @property
    def id(self) -> int:
        return self.message_id
