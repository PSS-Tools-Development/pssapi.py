from .entity_base import EntityWithIdBase
from .raw import UserRaw


class User(UserRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.id_


__all__ = [
    "User",
]
