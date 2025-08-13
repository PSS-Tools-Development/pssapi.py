"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class ShipDesignRaw(EntityBaseRaw, tag="ShipDesign"):
    XML_NODE_NAME: str = "ShipDesign"

    allow_interacial: Optional[bool] = attr(name="AllowInteracial", default=None)
    background_asset_id: Optional[int] = attr(name="BackgroundAssetId", default=None)
    columns: Optional[int] = attr(name="Columns", default=None)
    door_frame_left_file_id: Optional[int] = attr(name="DoorFrameLeftFileId", default=None)
    door_frame_left_sprite_id: Optional[int] = attr(name="DoorFrameLeftSpriteId", default=None)
    door_frame_right_file_id: Optional[int] = attr(name="DoorFrameRightFileId", default=None)
    door_frame_right_sprite_id: Optional[int] = attr(name="DoorFrameRightSpriteId", default=None)
    engine_x: Optional[int] = attr(name="EngineX", default=None)
    engine_y: Optional[int] = attr(name="EngineY", default=None)
    equipment_capacity: Optional[int] = attr(name="EquipmentCapacity", default=None)
    exterior_file_id: Optional[int] = attr(name="ExteriorFileId", default=None)
    exterior_sprite_id: Optional[int] = attr(name="ExteriorSpriteId", default=None)
    flag_x: Optional[int] = attr(name="FlagX", default=None)
    flag_y: Optional[int] = attr(name="FlagY", default=None)
    foreground_asset_id: Optional[int] = attr(name="ForegroundAssetId", default=None)
    gas_capacity: Optional[int] = attr(name="GasCapacity", default=None)
    hp: Optional[int] = attr(name="Hp", default=None)
    interior_file_id: Optional[int] = attr(name="InteriorFileId", default=None)
    interior_sprite_id: Optional[int] = attr(name="InteriorSpriteId", default=None)
    lift_file_id: Optional[int] = attr(name="LiftFileId", default=None)
    lift_sprite_id: Optional[int] = attr(name="LiftSpriteId", default=None)
    logo_file_id: Optional[int] = attr(name="LogoFileId", default=None)
    logo_sprite_id: Optional[int] = attr(name="LogoSpriteId", default=None)
    mask: Optional[str] = attr(name="Mask", default=None)
    mineral_capacity: Optional[int] = attr(name="MineralCapacity", default=None)
    mineral_cost: Optional[int] = attr(name="MineralCost", default=None)
    mini_ship_sprite_id: Optional[int] = attr(name="MiniShipSpriteId", default=None)
    race_id: Optional[int] = attr(name="RaceId", default=None)
    repair_time: Optional[int] = attr(name="RepairTime", default=None)
    required_research_design_id: Optional[int] = attr(name="RequiredResearchDesignId", default=None)
    required_ship_design_id: Optional[int] = attr(name="RequiredShipDesignId", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    room_frame_file_id: Optional[int] = attr(name="RoomFrameFileId", default=None)
    room_frame_sprite_id: Optional[int] = attr(name="RoomFrameSpriteId", default=None)
    rows: Optional[int] = attr(name="Rows", default=None)
    ship_description: Optional[str] = attr(name="ShipDescription", default=None)
    ship_design_id: Optional[int] = attr(name="ShipDesignId", default=None)
    ship_design_name: Optional[str] = attr(name="ShipDesignName", default=None)
    ship_level: Optional[int] = attr(name="ShipLevel", default=None)
    ship_type: Optional[str] = attr(name="ShipType", default=None)
    starbux_cost: Optional[int] = attr(name="StarbuxCost", default=None)
    thrust_line_animation_id: Optional[int] = attr(name="ThrustLineAnimationId", default=None)
    thrust_particle_sprite_id: Optional[int] = attr(name="ThrustParticleSpriteId", default=None)
    thrust_scale: Optional[float] = attr(name="ThrustScale", default=None)
    unlock_cost: Optional[str] = attr(name="UnlockCost", default=None)
    unlock_from_ship_design_id: Optional[int] = attr(name="UnlockFromShipDesignId", default=None)
    upgrade_cost: Optional[str] = attr(name="UpgradeCost", default=None)
    upgrade_offset_columns: Optional[int] = attr(name="UpgradeOffsetColumns", default=None)
    upgrade_offset_rows: Optional[int] = attr(name="UpgradeOffsetRows", default=None)
    upgrade_time: Optional[int] = attr(name="UpgradeTime", default=None)
    visibility_flags: Optional[str] = attr(name="VisibilityFlags", default=None)

    def _key(self):
        return (
            self.allow_interacial,
            self.background_asset_id,
            self.columns,
            self.door_frame_left_file_id,
            self.door_frame_left_sprite_id,
            self.door_frame_right_file_id,
            self.door_frame_right_sprite_id,
            self.engine_x,
            self.engine_y,
            self.equipment_capacity,
            self.exterior_file_id,
            self.exterior_sprite_id,
            self.flag_x,
            self.flag_y,
            self.foreground_asset_id,
            self.gas_capacity,
            self.hp,
            self.interior_file_id,
            self.interior_sprite_id,
            self.lift_file_id,
            self.lift_sprite_id,
            self.logo_file_id,
            self.logo_sprite_id,
            self.mask,
            self.mineral_capacity,
            self.mineral_cost,
            self.mini_ship_sprite_id,
            self.race_id,
            self.repair_time,
            self.required_research_design_id,
            self.required_ship_design_id,
            self.requirement_string,
            self.room_frame_file_id,
            self.room_frame_sprite_id,
            self.rows,
            self.ship_description,
            self.ship_design_id,
            self.ship_design_name,
            self.ship_level,
            self.ship_type,
            self.starbux_cost,
            self.thrust_line_animation_id,
            self.thrust_particle_sprite_id,
            self.thrust_scale,
            self.unlock_cost,
            self.unlock_from_ship_design_id,
            self.upgrade_cost,
            self.upgrade_offset_columns,
            self.upgrade_offset_rows,
            self.upgrade_time,
            self.visibility_flags,
        )


__all__ = [
    "ShipDesignRaw",
]
