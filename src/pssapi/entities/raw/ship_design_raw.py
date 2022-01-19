"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ShipDesignRaw:
    XML_NODE_NAME: str = "ShipDesign"

    def __init__(self, ship_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._allow_interacial: bool = _parse.pss_bool(ship_design_info.get("AllowInteracial"))
        self._background_asset_id: int = _parse.pss_int(ship_design_info.get("BackgroundAssetId"))
        self._columns: int = _parse.pss_int(ship_design_info.get("Columns"))
        self._door_frame_left_file_id: int = _parse.pss_int(ship_design_info.get("DoorFrameLeftFileId"))
        self._door_frame_left_sprite_id: int = _parse.pss_int(ship_design_info.get("DoorFrameLeftSpriteId"))
        self._door_frame_right_file_id: int = _parse.pss_int(ship_design_info.get("DoorFrameRightFileId"))
        self._door_frame_right_sprite_id: int = _parse.pss_int(ship_design_info.get("DoorFrameRightSpriteId"))
        self._engine_x: int = _parse.pss_int(ship_design_info.get("EngineX"))
        self._engine_y: int = _parse.pss_int(ship_design_info.get("EngineY"))
        self._equipment_capacity: int = _parse.pss_int(ship_design_info.get("EquipmentCapacity"))
        self._exterior_file_id: int = _parse.pss_int(ship_design_info.get("ExteriorFileId"))
        self._exterior_sprite_id: int = _parse.pss_int(ship_design_info.get("ExteriorSpriteId"))
        self._flag_x: int = _parse.pss_int(ship_design_info.get("FlagX"))
        self._flag_y: int = _parse.pss_int(ship_design_info.get("FlagY"))
        self._foreground_asset_id: int = _parse.pss_int(ship_design_info.get("ForegroundAssetId"))
        self._gas_capacity: int = _parse.pss_int(ship_design_info.get("GasCapacity"))
        self._hp: int = _parse.pss_int(ship_design_info.get("Hp"))
        self._interior_file_id: int = _parse.pss_int(ship_design_info.get("InteriorFileId"))
        self._interior_sprite_id: int = _parse.pss_int(ship_design_info.get("InteriorSpriteId"))
        self._lift_file_id: int = _parse.pss_int(ship_design_info.get("LiftFileId"))
        self._lift_sprite_id: int = _parse.pss_int(ship_design_info.get("LiftSpriteId"))
        self._logo_file_id: int = _parse.pss_int(ship_design_info.get("LogoFileId"))
        self._logo_sprite_id: int = _parse.pss_int(ship_design_info.get("LogoSpriteId"))
        self._mask: str = _parse.pss_str(ship_design_info.get("Mask"))
        self._mineral_capacity: int = _parse.pss_int(ship_design_info.get("MineralCapacity"))
        self._mineral_cost: int = _parse.pss_int(ship_design_info.get("MineralCost"))
        self._mini_ship_sprite_id: int = _parse.pss_int(ship_design_info.get("MiniShipSpriteId"))
        self._race_id: int = _parse.pss_int(ship_design_info.get("RaceId"))
        self._repair_time: int = _parse.pss_int(ship_design_info.get("RepairTime"))
        self._required_research_design_id: int = _parse.pss_int(ship_design_info.get("RequiredResearchDesignId"))
        self._required_ship_design_id: int = _parse.pss_int(ship_design_info.get("RequiredShipDesignId"))
        self._requirement_string: str = _parse.pss_str(ship_design_info.get("RequirementString"))
        self._room_frame_file_id: int = _parse.pss_int(ship_design_info.get("RoomFrameFileId"))
        self._room_frame_sprite_id: int = _parse.pss_int(ship_design_info.get("RoomFrameSpriteId"))
        self._rows: int = _parse.pss_int(ship_design_info.get("Rows"))
        self._ship_description: str = _parse.pss_str(ship_design_info.get("ShipDescription"))
        self._ship_design_id: int = _parse.pss_int(ship_design_info.get("ShipDesignId"))
        self._ship_design_name: str = _parse.pss_str(ship_design_info.get("ShipDesignName"))
        self._ship_level: int = _parse.pss_int(ship_design_info.get("ShipLevel"))
        self._ship_type: str = _parse.pss_str(ship_design_info.get("ShipType"))
        self._starbux_cost: int = _parse.pss_int(ship_design_info.get("StarbuxCost"))
        self._thrust_line_animation_id: int = _parse.pss_int(ship_design_info.get("ThrustLineAnimationId"))
        self._thrust_particle_sprite_id: int = _parse.pss_int(ship_design_info.get("ThrustParticleSpriteId"))
        self._thrust_scale: float = _parse.pss_float(ship_design_info.get("ThrustScale"))
        self._unlock_cost: str = _parse.pss_str(ship_design_info.get("UnlockCost"))
        self._unlock_from_ship_design_id: int = _parse.pss_int(ship_design_info.get("UnlockFromShipDesignId"))
        self._upgrade_cost: str = _parse.pss_str(ship_design_info.get("UpgradeCost"))
        self._upgrade_offset_columns: int = _parse.pss_int(ship_design_info.get("UpgradeOffsetColumns"))
        self._upgrade_offset_rows: int = _parse.pss_int(ship_design_info.get("UpgradeOffsetRows"))
        self._upgrade_time: int = _parse.pss_int(ship_design_info.get("UpgradeTime"))
        self._visibility_flags: str = _parse.pss_str(ship_design_info.get("VisibilityFlags"))

    @property
    def allow_interacial(self) -> bool:
        return self._allow_interacial

    @property
    def background_asset_id(self) -> int:
        return self._background_asset_id

    @property
    def columns(self) -> int:
        return self._columns

    @property
    def door_frame_left_file_id(self) -> int:
        return self._door_frame_left_file_id

    @property
    def door_frame_left_sprite_id(self) -> int:
        return self._door_frame_left_sprite_id

    @property
    def door_frame_right_file_id(self) -> int:
        return self._door_frame_right_file_id

    @property
    def door_frame_right_sprite_id(self) -> int:
        return self._door_frame_right_sprite_id

    @property
    def engine_x(self) -> int:
        return self._engine_x

    @property
    def engine_y(self) -> int:
        return self._engine_y

    @property
    def equipment_capacity(self) -> int:
        return self._equipment_capacity

    @property
    def exterior_file_id(self) -> int:
        return self._exterior_file_id

    @property
    def exterior_sprite_id(self) -> int:
        return self._exterior_sprite_id

    @property
    def flag_x(self) -> int:
        return self._flag_x

    @property
    def flag_y(self) -> int:
        return self._flag_y

    @property
    def foreground_asset_id(self) -> int:
        return self._foreground_asset_id

    @property
    def gas_capacity(self) -> int:
        return self._gas_capacity

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def interior_file_id(self) -> int:
        return self._interior_file_id

    @property
    def interior_sprite_id(self) -> int:
        return self._interior_sprite_id

    @property
    def lift_file_id(self) -> int:
        return self._lift_file_id

    @property
    def lift_sprite_id(self) -> int:
        return self._lift_sprite_id

    @property
    def logo_file_id(self) -> int:
        return self._logo_file_id

    @property
    def logo_sprite_id(self) -> int:
        return self._logo_sprite_id

    @property
    def mask(self) -> str:
        return self._mask

    @property
    def mineral_capacity(self) -> int:
        return self._mineral_capacity

    @property
    def mineral_cost(self) -> int:
        return self._mineral_cost

    @property
    def mini_ship_sprite_id(self) -> int:
        return self._mini_ship_sprite_id

    @property
    def race_id(self) -> int:
        return self._race_id

    @property
    def repair_time(self) -> int:
        return self._repair_time

    @property
    def required_research_design_id(self) -> int:
        return self._required_research_design_id

    @property
    def required_ship_design_id(self) -> int:
        return self._required_ship_design_id

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def room_frame_file_id(self) -> int:
        return self._room_frame_file_id

    @property
    def room_frame_sprite_id(self) -> int:
        return self._room_frame_sprite_id

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def ship_description(self) -> str:
        return self._ship_description

    @property
    def ship_design_id(self) -> int:
        return self._ship_design_id

    @property
    def ship_design_name(self) -> str:
        return self._ship_design_name

    @property
    def ship_level(self) -> int:
        return self._ship_level

    @property
    def ship_type(self) -> str:
        return self._ship_type

    @property
    def starbux_cost(self) -> int:
        return self._starbux_cost

    @property
    def thrust_line_animation_id(self) -> int:
        return self._thrust_line_animation_id

    @property
    def thrust_particle_sprite_id(self) -> int:
        return self._thrust_particle_sprite_id

    @property
    def thrust_scale(self) -> float:
        return self._thrust_scale

    @property
    def unlock_cost(self) -> str:
        return self._unlock_cost

    @property
    def unlock_from_ship_design_id(self) -> int:
        return self._unlock_from_ship_design_id

    @property
    def upgrade_cost(self) -> str:
        return self._upgrade_cost

    @property
    def upgrade_offset_columns(self) -> int:
        return self._upgrade_offset_columns

    @property
    def upgrade_offset_rows(self) -> int:
        return self._upgrade_offset_rows

    @property
    def upgrade_time(self) -> int:
        return self._upgrade_time

    @property
    def visibility_flags(self) -> str:
        return self._visibility_flags

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

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AllowInteracial": self.allow_interacial,
                "BackgroundAssetId": self.background_asset_id,
                "Columns": self.columns,
                "DoorFrameLeftFileId": self.door_frame_left_file_id,
                "DoorFrameLeftSpriteId": self.door_frame_left_sprite_id,
                "DoorFrameRightFileId": self.door_frame_right_file_id,
                "DoorFrameRightSpriteId": self.door_frame_right_sprite_id,
                "EngineX": self.engine_x,
                "EngineY": self.engine_y,
                "EquipmentCapacity": self.equipment_capacity,
                "ExteriorFileId": self.exterior_file_id,
                "ExteriorSpriteId": self.exterior_sprite_id,
                "FlagX": self.flag_x,
                "FlagY": self.flag_y,
                "ForegroundAssetId": self.foreground_asset_id,
                "GasCapacity": self.gas_capacity,
                "Hp": self.hp,
                "InteriorFileId": self.interior_file_id,
                "InteriorSpriteId": self.interior_sprite_id,
                "LiftFileId": self.lift_file_id,
                "LiftSpriteId": self.lift_sprite_id,
                "LogoFileId": self.logo_file_id,
                "LogoSpriteId": self.logo_sprite_id,
                "Mask": self.mask,
                "MineralCapacity": self.mineral_capacity,
                "MineralCost": self.mineral_cost,
                "MiniShipSpriteId": self.mini_ship_sprite_id,
                "RaceId": self.race_id,
                "RepairTime": self.repair_time,
                "RequiredResearchDesignId": self.required_research_design_id,
                "RequiredShipDesignId": self.required_ship_design_id,
                "RequirementString": self.requirement_string,
                "RoomFrameFileId": self.room_frame_file_id,
                "RoomFrameSpriteId": self.room_frame_sprite_id,
                "Rows": self.rows,
                "ShipDescription": self.ship_description,
                "ShipDesignId": self.ship_design_id,
                "ShipDesignName": self.ship_design_name,
                "ShipLevel": self.ship_level,
                "ShipType": self.ship_type,
                "StarbuxCost": self.starbux_cost,
                "ThrustLineAnimationId": self.thrust_line_animation_id,
                "ThrustParticleSpriteId": self.thrust_particle_sprite_id,
                "ThrustScale": self.thrust_scale,
                "UnlockCost": self.unlock_cost,
                "UnlockFromShipDesignId": self.unlock_from_ship_design_id,
                "UpgradeCost": self.upgrade_cost,
                "UpgradeOffsetColumns": self.upgrade_offset_columns,
                "UpgradeOffsetRows": self.upgrade_offset_rows,
                "UpgradeTime": self.upgrade_time,
                "VisibilityFlags": self.visibility_flags,
            }

        return self._dict
