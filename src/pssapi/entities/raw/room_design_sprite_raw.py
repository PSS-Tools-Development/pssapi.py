"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class RoomDesignSpriteRaw(EntityBaseRaw, tag="RoomDesignSprite"):
    XML_NODE_NAME: str = "RoomDesignSprite"

    animation_id: Optional[int] = attr(name="AnimationId", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    race_id: Optional[int] = attr(name="RaceId", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    room_design_id: Optional[int] = attr(name="RoomDesignId", default=None)
    room_design_sprite_id: Optional[int] = attr(name="RoomDesignSpriteId", default=None)
    room_effect_parameter: Optional[int] = attr(name="RoomEffectParameter", default=None)
    room_effect_type: Optional[str] = attr(name="RoomEffectType", default=None)
    room_sprite_type: Optional[str] = attr(name="RoomSpriteType", default=None)
    skin_description: Optional[str] = attr(name="SkinDescription", default=None)
    skin_key: Optional[int] = attr(name="SkinKey", default=None)
    skin_name: Optional[str] = attr(name="SkinName", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)

    def _key(self):
        return (
            self.animation_id,
            self.flags,
            self.metadata,
            self.race_id,
            self.requirement_string,
            self.room_design_id,
            self.room_design_sprite_id,
            self.room_effect_parameter,
            self.room_effect_type,
            self.room_sprite_type,
            self.skin_description,
            self.skin_key,
            self.skin_name,
            self.sprite_id,
        )


__all__ = [
    "RoomDesignSpriteRaw",
]
