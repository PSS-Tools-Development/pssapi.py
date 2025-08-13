from .entity_base import EntityWithIdBase
from .raw import SkinRaw


class Skin(SkinRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.skin_id


__all__ = [
    "Skin",
]
