"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class CollectionDesignRaw(EntityBaseRaw, tag="CollectionDesign"):
    XML_NODE_NAME: str = "CollectionDesign"

    ability_icon_sprite_id: Optional[int] = attr(name="AbilityIconSpriteId", default=None)
    ability_name: Optional[str] = attr(name="AbilityName", default=None)
    argument: Optional[int] = attr(name="Argument", default=None)
    base_chance: Optional[int] = attr(name="BaseChance", default=None)
    base_enhancement_value: Optional[int] = attr(name="BaseEnhancementValue", default=None)
    collection_description: Optional[str] = attr(name="CollectionDescription", default=None)
    collection_design_id: Optional[int] = attr(name="CollectionDesignId", default=None)
    collection_name: Optional[str] = attr(name="CollectionName", default=None)
    collection_type: Optional[str] = attr(name="CollectionType", default=None)
    color_string: Optional[str] = attr(name="ColorString", default=None)
    cooldown_time: Optional[int] = attr(name="CooldownTime", default=None)
    enhancement_type: Optional[str] = attr(name="EnhancementType", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    halo_animation_id: Optional[int] = attr(name="HaloAnimationId", default=None)
    icon_sprite_id: Optional[int] = attr(name="IconSpriteId", default=None)
    max_combo: Optional[int] = attr(name="MaxCombo", default=None)
    max_use: Optional[int] = attr(name="MaxUse", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    min_combo: Optional[int] = attr(name="MinCombo", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)
    step_chance: Optional[int] = attr(name="StepChance", default=None)
    step_enhancement_value: Optional[float] = attr(name="StepEnhancementValue", default=None)
    trigger_animation_id: Optional[int] = attr(name="TriggerAnimationId", default=None)
    trigger_type: Optional[str] = attr(name="TriggerType", default=None)

    def _key(self):
        return (
            self.ability_icon_sprite_id,
            self.ability_name,
            self.argument,
            self.base_chance,
            self.base_enhancement_value,
            self.collection_description,
            self.collection_design_id,
            self.collection_name,
            self.collection_type,
            self.color_string,
            self.cooldown_time,
            self.enhancement_type,
            self.flags,
            self.halo_animation_id,
            self.icon_sprite_id,
            self.max_combo,
            self.max_use,
            self.metadata,
            self.min_combo,
            self.sprite_id,
            self.step_chance,
            self.step_enhancement_value,
            self.trigger_animation_id,
            self.trigger_type,
        )


__all__ = [
    "CollectionDesignRaw",
]
