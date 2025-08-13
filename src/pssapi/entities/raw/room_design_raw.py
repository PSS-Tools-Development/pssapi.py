"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class RoomDesignRaw(EntityBaseRaw, tag="RoomDesign"):
    XML_NODE_NAME: str = "RoomDesign"

    activation_delay: Optional[int] = attr(name="ActivationDelay", default=None)
    capacity: Optional[int] = attr(name="Capacity", default=None)
    category_type: Optional[str] = attr(name="CategoryType", default=None)
    columns: Optional[int] = attr(name="Columns", default=None)
    construction_sprite_id: Optional[int] = attr(name="ConstructionSpriteId", default=None)
    construction_time: Optional[int] = attr(name="ConstructionTime", default=None)
    cooldown_time: Optional[int] = attr(name="CooldownTime", default=None)
    craft_design_id: Optional[int] = attr(name="CraftDesignId", default=None)
    default_defence_bonus: Optional[int] = attr(name="DefaultDefenceBonus", default=None)
    enhancement_type: Optional[str] = attr(name="EnhancementType", default=None)
    exterior_asset_id: Optional[int] = attr(name="ExteriorAssetId", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    flip_on_enemy_ship: Optional[bool] = attr(name="FlipOnEnemyShip", default=None)
    image_sprite_id: Optional[int] = attr(name="ImageSpriteId", default=None)
    improvement_amounts: Optional[int] = attr(name="ImprovementAmounts", default=None)
    interior_asset_id: Optional[int] = attr(name="InteriorAssetId", default=None)
    item_rank: Optional[int] = attr(name="ItemRank", default=None)
    level: Optional[int] = attr(name="Level", default=None)
    logo_sprite_id: Optional[int] = attr(name="LogoSpriteId", default=None)
    manufacture_capacity: Optional[int] = attr(name="ManufactureCapacity", default=None)
    manufacture_rate: Optional[float] = attr(name="ManufactureRate", default=None)
    manufacture_type: Optional[str] = attr(name="ManufactureType", default=None)
    max_count: Optional[int] = attr(name="MaxCount", default=None)
    max_power_generated: Optional[int] = attr(name="MaxPowerGenerated", default=None)
    max_system_power: Optional[int] = attr(name="MaxSystemPower", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    min_range: Optional[int] = attr(name="MinRange", default=None)
    min_ship_level: Optional[int] = attr(name="MinShipLevel", default=None)
    missile_design_id: Optional[int] = attr(name="MissileDesignId", default=None)
    price_string: Optional[str] = attr(name="PriceString", default=None)
    random_improvements: Optional[int] = attr(name="RandomImprovements", default=None)
    range: Optional[int] = attr(name="Range", default=None)
    refill_cost_string: Optional[str] = attr(name="RefillCostString", default=None)
    refill_unit_cost: Optional[int] = attr(name="RefillUnitCost", default=None)
    reload_time: Optional[int] = attr(name="ReloadTime", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    room_description: Optional[str] = attr(name="RoomDescription", default=None)
    room_design_id: Optional[int] = attr(name="RoomDesignId", default=None)
    room_name: Optional[str] = attr(name="RoomName", default=None)
    room_short_name: Optional[str] = attr(name="RoomShortName", default=None)
    room_type: Optional[str] = attr(name="RoomType", default=None)
    room_variant_type: Optional[int] = attr(name="RoomVariantType", default=None)
    root_room_design_id: Optional[int] = attr(name="RootRoomDesignId", default=None)
    rotate: Optional[bool] = attr(name="Rotate", default=None)
    rows: Optional[int] = attr(name="Rows", default=None)
    sort_index: Optional[int] = attr(name="SortIndex", default=None)
    supported_grid_types: Optional[int] = attr(name="SupportedGridTypes", default=None)
    tags: Optional[str] = attr(name="Tags", default=None)
    target_type: Optional[str] = attr(name="TargetType", default=None)
    upgrade_from_room_design_id: Optional[int] = attr(name="UpgradeFromRoomDesignId", default=None)

    def _key(self):
        return (
            self.activation_delay,
            self.capacity,
            self.category_type,
            self.columns,
            self.construction_sprite_id,
            self.construction_time,
            self.cooldown_time,
            self.craft_design_id,
            self.default_defence_bonus,
            self.enhancement_type,
            self.exterior_asset_id,
            self.flags,
            self.flip_on_enemy_ship,
            self.image_sprite_id,
            self.improvement_amounts,
            self.interior_asset_id,
            self.item_rank,
            self.level,
            self.logo_sprite_id,
            self.manufacture_capacity,
            self.manufacture_rate,
            self.manufacture_type,
            self.max_count,
            self.max_power_generated,
            self.max_system_power,
            self.metadata,
            self.min_range,
            self.min_ship_level,
            self.missile_design_id,
            self.price_string,
            self.random_improvements,
            self.range,
            self.refill_cost_string,
            self.refill_unit_cost,
            self.reload_time,
            self.requirement_string,
            self.room_description,
            self.room_design_id,
            self.room_name,
            self.room_short_name,
            self.room_type,
            self.room_variant_type,
            self.root_room_design_id,
            self.rotate,
            self.rows,
            self.sort_index,
            self.supported_grid_types,
            self.tags,
            self.target_type,
            self.upgrade_from_room_design_id,
        )


__all__ = [
    "RoomDesignRaw",
]
