"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ShipDesignRaw:
    XML_NODE_NAME: str = 'ShipDesign'

    def __init__(self, ship_design_info: _EntityInfo) -> None:
        self.allow_interacial: bool = _parse.pss_bool(ship_design_info.get('AllowInteracial'))
        self.background_asset_id: int = _parse.pss_int(ship_design_info.get('BackgroundAssetId'))
        self.columns: int = _parse.pss_int(ship_design_info.get('Columns'))
        self.door_frame_left_file_id: int = _parse.pss_int(ship_design_info.get('DoorFrameLeftFileId'))
        self.door_frame_left_sprite_id: int = _parse.pss_int(ship_design_info.get('DoorFrameLeftSpriteId'))
        self.door_frame_right_file_id: int = _parse.pss_int(ship_design_info.get('DoorFrameRightFileId'))
        self.door_frame_right_sprite_id: int = _parse.pss_int(ship_design_info.get('DoorFrameRightSpriteId'))
        self.engine_x: int = _parse.pss_int(ship_design_info.get('EngineX'))
        self.engine_y: int = _parse.pss_int(ship_design_info.get('EngineY'))
        self.equipment_capacity: int = _parse.pss_int(ship_design_info.get('EquipmentCapacity'))
        self.exterior_file_id: int = _parse.pss_int(ship_design_info.get('ExteriorFileId'))
        self.exterior_sprite_id: int = _parse.pss_int(ship_design_info.get('ExteriorSpriteId'))
        self.flag_x: int = _parse.pss_int(ship_design_info.get('FlagX'))
        self.flag_y: int = _parse.pss_int(ship_design_info.get('FlagY'))
        self.foreground_asset_id: int = _parse.pss_int(ship_design_info.get('ForegroundAssetId'))
        self.gas_capacity: int = _parse.pss_int(ship_design_info.get('GasCapacity'))
        self.hp: int = _parse.pss_int(ship_design_info.get('Hp'))
        self.interior_file_id: int = _parse.pss_int(ship_design_info.get('InteriorFileId'))
        self.interior_sprite_id: int = _parse.pss_int(ship_design_info.get('InteriorSpriteId'))
        self.lift_file_id: int = _parse.pss_int(ship_design_info.get('LiftFileId'))
        self.lift_sprite_id: int = _parse.pss_int(ship_design_info.get('LiftSpriteId'))
        self.logo_file_id: int = _parse.pss_int(ship_design_info.get('LogoFileId'))
        self.logo_sprite_id: int = _parse.pss_int(ship_design_info.get('LogoSpriteId'))
        self.mask: str = _parse.pss_str(ship_design_info.get('Mask'))
        self.mineral_capacity: int = _parse.pss_int(ship_design_info.get('MineralCapacity'))
        self.mineral_cost: int = _parse.pss_int(ship_design_info.get('MineralCost'))
        self.mini_ship_sprite_id: int = _parse.pss_int(ship_design_info.get('MiniShipSpriteId'))
        self.race_id: int = _parse.pss_int(ship_design_info.get('RaceId'))
        self.repair_time: int = _parse.pss_int(ship_design_info.get('RepairTime'))
        self.required_research_design_id: int = _parse.pss_int(ship_design_info.get('RequiredResearchDesignId'))
        self.required_ship_design_id: int = _parse.pss_int(ship_design_info.get('RequiredShipDesignId'))
        self.requirement_string: str = _parse.pss_str(ship_design_info.get('RequirementString'))
        self.room_frame_file_id: int = _parse.pss_int(ship_design_info.get('RoomFrameFileId'))
        self.room_frame_sprite_id: int = _parse.pss_int(ship_design_info.get('RoomFrameSpriteId'))
        self.rows: int = _parse.pss_int(ship_design_info.get('Rows'))
        self.ship_description: str = _parse.pss_str(ship_design_info.get('ShipDescription'))
        self.ship_design_id: int = _parse.pss_int(ship_design_info.get('ShipDesignId'))
        self.ship_design_name: str = _parse.pss_str(ship_design_info.get('ShipDesignName'))
        self.ship_level: int = _parse.pss_int(ship_design_info.get('ShipLevel'))
        self.ship_type: str = _parse.pss_str(ship_design_info.get('ShipType'))
        self.starbux_cost: int = _parse.pss_int(ship_design_info.get('StarbuxCost'))
        self.thrust_line_animation_id: int = _parse.pss_int(ship_design_info.get('ThrustLineAnimationId'))
        self.thrust_particle_sprite_id: int = _parse.pss_int(ship_design_info.get('ThrustParticleSpriteId'))
        self.thrust_scale: float = _parse.pss_float(ship_design_info.get('ThrustScale'))
        self.unlock_cost: str = _parse.pss_str(ship_design_info.get('UnlockCost'))
        self.unlock_from_ship_design_id: int = _parse.pss_int(ship_design_info.get('UnlockFromShipDesignId'))
        self.upgrade_cost: str = _parse.pss_str(ship_design_info.get('UpgradeCost'))
        self.upgrade_offset_columns: int = _parse.pss_int(ship_design_info.get('UpgradeOffsetColumns'))
        self.upgrade_offset_rows: int = _parse.pss_int(ship_design_info.get('UpgradeOffsetRows'))
        self.upgrade_time: int = _parse.pss_int(ship_design_info.get('UpgradeTime'))
        self.visibility_flags: str = _parse.pss_str(ship_design_info.get('VisibilityFlags'))
