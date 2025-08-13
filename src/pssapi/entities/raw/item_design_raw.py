"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class ItemDesignRaw(EntityBaseRaw, tag="ItemDesign"):
    XML_NODE_NAME: str = "ItemDesign"

    active_animation_id: Optional[int] = attr(name="ActiveAnimationId", default=None)
    animation_id: Optional[int] = attr(name="AnimationId", default=None)
    border_sprite_id: Optional[int] = attr(name="BorderSpriteId", default=None)
    build_price: Optional[int] = attr(name="BuildPrice", default=None)
    build_time: Optional[int] = attr(name="BuildTime", default=None)
    character_design_id: Optional[int] = attr(name="CharacterDesignId", default=None)
    character_part_id: Optional[int] = attr(name="CharacterPartId", default=None)
    circulation: Optional[int] = attr(name="Circulation", default=None)
    content: Optional[str] = attr(name="Content", default=None)
    craft_design_id: Optional[int] = attr(name="CraftDesignId", default=None)
    drop_chance: Optional[int] = attr(name="DropChance", default=None)
    enhancement_type: Optional[str] = attr(name="EnhancementType", default=None)
    enhancement_value: Optional[float] = attr(name="EnhancementValue", default=None)
    equip_sound_file_id: Optional[int] = attr(name="EquipSoundFileId", default=None)
    fair_price: Optional[int] = attr(name="FairPrice", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    gas_cost: Optional[int] = attr(name="GasCost", default=None)
    image_sprite_id: Optional[int] = attr(name="ImageSpriteId", default=None)
    ingredients: Optional[str] = attr(name="Ingredients", default=None)
    item_design_description: Optional[str] = attr(name="ItemDesignDescription", default=None)
    item_design_id: Optional[int] = attr(name="ItemDesignId", default=None)
    item_design_key: Optional[str] = attr(name="ItemDesignKey", default=None)
    item_design_name: Optional[str] = attr(name="ItemDesignName", default=None)
    item_design_name_en: Optional[str] = attr(name="ItemDesignNameEN", default=None)
    item_space: Optional[int] = attr(name="ItemSpace", default=None)
    item_sub_type: Optional[str] = attr(name="ItemSubType", default=None)
    item_type: Optional[str] = attr(name="ItemType", default=None)
    level: Optional[int] = attr(name="Level", default=None)
    logo_sprite_id: Optional[int] = attr(name="LogoSpriteId", default=None)
    manufacture_cost: Optional[str] = attr(name="ManufactureCost", default=None)
    market_price: Optional[int] = attr(name="MarketPrice", default=None)
    max_count: Optional[int] = attr(name="MaxCount", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    min_room_level: Optional[int] = attr(name="MinRoomLevel", default=None)
    min_ship_level: Optional[int] = attr(name="MinShipLevel", default=None)
    mineral_cost: Optional[int] = attr(name="MineralCost", default=None)
    missile_design_id: Optional[int] = attr(name="MissileDesignId", default=None)
    module_argument: Optional[int] = attr(name="ModuleArgument", default=None)
    module_type: Optional[str] = attr(name="ModuleType", default=None)
    our_price: Optional[int] = attr(name="OurPrice", default=None)
    parent_item_design_id: Optional[int] = attr(name="ParentItemDesignId", default=None)
    particle_sprite_id: Optional[int] = attr(name="ParticleSpriteId", default=None)
    priority: Optional[int] = attr(name="Priority", default=None)
    race_id: Optional[int] = attr(name="RaceId", default=None)
    rank: Optional[int] = attr(name="Rank", default=None)
    rarity: Optional[str] = attr(name="Rarity", default=None)
    reload_modifier: Optional[int] = attr(name="ReloadModifier", default=None)
    reload_time: Optional[int] = attr(name="ReloadTime", default=None)
    required_research_design_id: Optional[int] = attr(name="RequiredResearchDesignId", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    room_design_id: Optional[int] = attr(name="RoomDesignId", default=None)
    root_item_design_id: Optional[int] = attr(name="RootItemDesignId", default=None)
    situation_design_id: Optional[int] = attr(name="SituationDesignId", default=None)
    sound_file_id: Optional[int] = attr(name="SoundFileId", default=None)
    tags: Optional[str] = attr(name="Tags", default=None)
    training_design_id: Optional[int] = attr(name="TrainingDesignId", default=None)
    transaction_volume: Optional[int] = attr(name="TransactionVolume", default=None)

    def _key(self):
        return (
            self.active_animation_id,
            self.animation_id,
            self.border_sprite_id,
            self.build_price,
            self.build_time,
            self.character_design_id,
            self.character_part_id,
            self.circulation,
            self.content,
            self.craft_design_id,
            self.drop_chance,
            self.enhancement_type,
            self.enhancement_value,
            self.equip_sound_file_id,
            self.fair_price,
            self.flags,
            self.gas_cost,
            self.image_sprite_id,
            self.ingredients,
            self.item_design_description,
            self.item_design_id,
            self.item_design_key,
            self.item_design_name,
            self.item_design_name_en,
            self.item_space,
            self.item_sub_type,
            self.item_type,
            self.level,
            self.logo_sprite_id,
            self.manufacture_cost,
            self.market_price,
            self.max_count,
            self.metadata,
            self.min_room_level,
            self.min_ship_level,
            self.mineral_cost,
            self.missile_design_id,
            self.module_argument,
            self.module_type,
            self.our_price,
            self.parent_item_design_id,
            self.particle_sprite_id,
            self.priority,
            self.race_id,
            self.rank,
            self.rarity,
            self.reload_modifier,
            self.reload_time,
            self.required_research_design_id,
            self.requirement_string,
            self.room_design_id,
            self.root_item_design_id,
            self.situation_design_id,
            self.sound_file_id,
            self.tags,
            self.training_design_id,
            self.transaction_volume,
        )


__all__ = [
    "ItemDesignRaw",
]
