from .entity_base import EntityWithIdBase
from .raw import RoomDesignSpriteRaw


class RoomDesignSprite(RoomDesignSpriteRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.room_design_sprite_id


__all__ = [
    "RoomDesignSprite",
]
