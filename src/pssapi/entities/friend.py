from .entity_base import EntityWithIdBase
from .raw import FriendRaw


class Friend(FriendRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.id_


__all__ = [
    "Friend",
]
