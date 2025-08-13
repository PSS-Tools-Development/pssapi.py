"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class AnimationRaw(EntityBaseRaw, tag="Animation"):
    XML_NODE_NAME: str = "Animation"

    animation_effect_type: Optional[str] = attr(name="AnimationEffectType", default=None)
    animation_id: Optional[int] = attr(name="AnimationId", default=None)
    animation_sprites: Optional[str] = attr(name="AnimationSprites", default=None)
    duration: Optional[int] = attr(name="Duration", default=None)
    key: Optional[str] = attr(name="Key", default=None)

    def _key(self):
        return (
            self.animation_effect_type,
            self.animation_id,
            self.animation_sprites,
            self.duration,
            self.key,
        )


__all__ = [
    "AnimationRaw",
]
