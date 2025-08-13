from .entity_base import EntityWithIdBase
from .raw import SpriteRaw


class Sprite(SpriteRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.sprite_id


__all__ = [
    "Sprite",
]
