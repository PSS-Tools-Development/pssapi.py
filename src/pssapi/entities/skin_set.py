from .entity_base import EntityWithIdBase
from .raw import SkinSetRaw


class SkinSet(SkinSetRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.skin_set_id


__all__ = [
    "SkinSet",
]
