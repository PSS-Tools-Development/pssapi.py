"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class BackgroundRaw(EntityBaseRaw, tag="Background"):
    XML_NODE_NAME: str = "Background"

    background_effect_type: Optional[str] = attr(name="BackgroundEffectType", default=None)
    background_id: Optional[int] = attr(name="BackgroundId", default=None)
    background_sprite_id: Optional[int] = attr(name="BackgroundSpriteId", default=None)
    background_type: Optional[str] = attr(name="BackgroundType", default=None)
    close_object_sprite_id: Optional[str] = attr(name="CloseObjectSpriteId", default=None)
    environment_float_argument: Optional[int] = attr(name="EnvironmentFloatArgument", default=None)
    environment_int_argument: Optional[int] = attr(name="EnvironmentIntArgument", default=None)
    environment_type: Optional[str] = attr(name="EnvironmentType", default=None)
    far_object_sprite_id: Optional[str] = attr(name="FarObjectSpriteId", default=None)
    hazard_argument: Optional[int] = attr(name="HazardArgument", default=None)
    hazard_category: Optional[str] = attr(name="HazardCategory", default=None)
    hazard_chance: Optional[int] = attr(name="HazardChance", default=None)
    hazard_effect_sprite_id: Optional[int] = attr(name="HazardEffectSpriteId", default=None)
    hazard_icon_sprite_id: Optional[int] = attr(name="HazardIconSpriteId", default=None)
    hazard_type: Optional[str] = attr(name="HazardType", default=None)
    is_active: Optional[bool] = attr(name="IsActive", default=None)
    max_hazard_interval: Optional[int] = attr(name="MaxHazardInterval", default=None)
    medium_object_sprite_id: Optional[str] = attr(name="MediumObjectSpriteId", default=None)
    min_hazard_interval: Optional[int] = attr(name="MinHazardInterval", default=None)
    music_file_id: Optional[int] = attr(name="MusicFileId", default=None)
    orbit_anchor_alignment: Optional[str] = attr(name="OrbitAnchorAlignment", default=None)
    orbit_animation_id: Optional[int] = attr(name="OrbitAnimationId", default=None)

    def _key(self):
        return (
            self.background_effect_type,
            self.background_id,
            self.background_sprite_id,
            self.background_type,
            self.close_object_sprite_id,
            self.environment_float_argument,
            self.environment_int_argument,
            self.environment_type,
            self.far_object_sprite_id,
            self.hazard_argument,
            self.hazard_category,
            self.hazard_chance,
            self.hazard_effect_sprite_id,
            self.hazard_icon_sprite_id,
            self.hazard_type,
            self.is_active,
            self.max_hazard_interval,
            self.medium_object_sprite_id,
            self.min_hazard_interval,
            self.music_file_id,
            self.orbit_anchor_alignment,
            self.orbit_animation_id,
        )


__all__ = [
    "BackgroundRaw",
]
