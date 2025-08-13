from .entity_base import EntityWithIdBase
from .raw import MessageRaw


class Message(MessageRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.message_id


__all__ = [
    "Message",
]
