####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ShipDesignRaw():
    XML_NODE_NAME: str = 'ShipDesign'

    def __init__(self, ship_design_info: _EntityInfo) -> None:
        self.__ship_design_id: int = _parse.pss_int(ship_design_info.get('ShipDesignId'))
        self.__ship_design_name: str = _parse.pss_str(ship_design_info.get('ShipDesignName'))
        self.__ship_description: str = _parse.pss_str(ship_design_info.get('ShipDescription'))
        self.__ship_level: int = _parse.pss_int(ship_design_info.get('ShipLevel'))
        self.__rows: int = _parse.pss_int(ship_design_info.get('Rows'))
        self.__columns: int = _parse.pss_int(ship_design_info.get('Columns'))
        self.__mask: int = _parse.pss_int(ship_design_info.get('Mask'))
        self.__hp: int = _parse.pss_int(ship_design_info.get('Hp'))
        self.__mineral_cost: int = _parse.pss_int(ship_design_info.get('MineralCost'))
        self.__repair_time: int = _parse.pss_int(ship_design_info.get('RepairTime'))
        self.__exterior_sprite_id: int = _parse.pss_int(ship_design_info.get('ExteriorSpriteId'))
        self.__interior_sprite_id: int = _parse.pss_int(ship_design_info.get('InteriorSpriteId'))
        self.__logo_sprite_id: int = _parse.pss_int(ship_design_info.get('LogoSpriteId'))
        self.__upgrade_time: int = _parse.pss_int(ship_design_info.get('UpgradeTime'))
        self.__room_frame_sprite_id: int = _parse.pss_int(ship_design_info.get('RoomFrameSpriteId'))
        self.__upgrade_offset_rows: int = _parse.pss_int(ship_design_info.get('UpgradeOffsetRows'))
        self.__upgrade_offset_columns: int = _parse.pss_int(ship_design_info.get('UpgradeOffsetColumns'))
        self.__lift_sprite_id: int = _parse.pss_int(ship_design_info.get('LiftSpriteId'))
        self.__door_frame_left_sprite_id: int = _parse.pss_int(ship_design_info.get('DoorFrameLeftSpriteId'))
        self.__door_frame_right_sprite_id: int = _parse.pss_int(ship_design_info.get('DoorFrameRightSpriteId'))
        self.__starbux_cost: int = _parse.pss_int(ship_design_info.get('StarbuxCost'))
        self.__engine_x: int = _parse.pss_int(ship_design_info.get('EngineX'))
        self.__engine_y: int = _parse.pss_int(ship_design_info.get('EngineY'))
        self.__mineral_capacity: int = _parse.pss_int(ship_design_info.get('MineralCapacity'))
        self.__gas_capacity: int = _parse.pss_int(ship_design_info.get('GasCapacity'))
        self.__thrust_scale: float = _parse.pss_float(ship_design_info.get('ThrustScale'))
        self.__flag_x: int = _parse.pss_int(ship_design_info.get('FlagX'))
        self.__flag_y: int = _parse.pss_int(ship_design_info.get('FlagY'))
        self.__mini_ship_sprite_id: int = _parse.pss_int(ship_design_info.get('MiniShipSpriteId'))
        self.__allow_interacial: bool = _parse.pss_bool(ship_design_info.get('AllowInteracial'))
        self.__equipment_capacity: int = _parse.pss_int(ship_design_info.get('EquipmentCapacity'))
        self.__ship_type: str = _parse.pss_str(ship_design_info.get('ShipType'))
        self.__upgrade_cost: str = _parse.pss_str(ship_design_info.get('UpgradeCost'))
        self.__unlock_cost: str = _parse.pss_str(ship_design_info.get('UnlockCost'))
        self.__requirement_string: str = _parse.pss_str(ship_design_info.get('RequirementString'))
        self.__visibility_flags: str = _parse.pss_str(ship_design_info.get('VisibilityFlags'))
        self.__unlock_from_ship_design_id: int = _parse.pss_int(ship_design_info.get('UnlockFromShipDesignId'))
        self.__required_research_design_id: int = _parse.pss_int(ship_design_info.get('RequiredResearchDesignId'))
        self.__thrust_particle_sprite_id: int = _parse.pss_int(ship_design_info.get('ThrustParticleSpriteId'))
        self.__thrust_line_animation_id: int = _parse.pss_int(ship_design_info.get('ThrustLineAnimationId'))
        self.__required_ship_design_id: int = _parse.pss_int(ship_design_info.get('RequiredShipDesignId'))
        self.__race_id: int = _parse.pss_int(ship_design_info.get('RaceId'))
        self.__exterior_file_id: int = _parse.pss_int(ship_design_info.get('ExteriorFileId'))
        self.__interior_file_id: int = _parse.pss_int(ship_design_info.get('InteriorFileId'))
        self.__logo_file_id: int = _parse.pss_int(ship_design_info.get('LogoFileId'))
        self.__room_frame_file_id: int = _parse.pss_int(ship_design_info.get('RoomFrameFileId'))
        self.__lift_file_id: int = _parse.pss_int(ship_design_info.get('LiftFileId'))
        self.__door_frame_left_file_id: int = _parse.pss_int(ship_design_info.get('DoorFrameLeftFileId'))
        self.__door_frame_right_file_id: int = _parse.pss_int(ship_design_info.get('DoorFrameRightFileId'))
        self.__foreground_asset_id: int = _parse.pss_int(ship_design_info.get('ForegroundAssetId'))
        self.__background_asset_id: int = _parse.pss_int(ship_design_info.get('BackgroundAssetId'))

    @property
    def ship_design_id(self) -> int:
        return self.__ship_design_id

    @property
    def ship_design_name(self) -> str:
        return self.__ship_design_name

    @property
    def ship_description(self) -> str:
        return self.__ship_description

    @property
    def ship_level(self) -> int:
        return self.__ship_level

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def columns(self) -> int:
        return self.__columns

    @property
    def mask(self) -> int:
        return self.__mask

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def mineral_cost(self) -> int:
        return self.__mineral_cost

    @property
    def repair_time(self) -> int:
        return self.__repair_time

    @property
    def exterior_sprite_id(self) -> int:
        return self.__exterior_sprite_id

    @property
    def interior_sprite_id(self) -> int:
        return self.__interior_sprite_id

    @property
    def logo_sprite_id(self) -> int:
        return self.__logo_sprite_id

    @property
    def upgrade_time(self) -> int:
        return self.__upgrade_time

    @property
    def room_frame_sprite_id(self) -> int:
        return self.__room_frame_sprite_id

    @property
    def upgrade_offset_rows(self) -> int:
        return self.__upgrade_offset_rows

    @property
    def upgrade_offset_columns(self) -> int:
        return self.__upgrade_offset_columns

    @property
    def lift_sprite_id(self) -> int:
        return self.__lift_sprite_id

    @property
    def door_frame_left_sprite_id(self) -> int:
        return self.__door_frame_left_sprite_id

    @property
    def door_frame_right_sprite_id(self) -> int:
        return self.__door_frame_right_sprite_id

    @property
    def starbux_cost(self) -> int:
        return self.__starbux_cost

    @property
    def engine_x(self) -> int:
        return self.__engine_x

    @property
    def engine_y(self) -> int:
        return self.__engine_y

    @property
    def mineral_capacity(self) -> int:
        return self.__mineral_capacity

    @property
    def gas_capacity(self) -> int:
        return self.__gas_capacity

    @property
    def thrust_scale(self) -> float:
        return self.__thrust_scale

    @property
    def flag_x(self) -> int:
        return self.__flag_x

    @property
    def flag_y(self) -> int:
        return self.__flag_y

    @property
    def mini_ship_sprite_id(self) -> int:
        return self.__mini_ship_sprite_id

    @property
    def allow_interacial(self) -> bool:
        return self.__allow_interacial

    @property
    def equipment_capacity(self) -> int:
        return self.__equipment_capacity

    @property
    def ship_type(self) -> str:
        return self.__ship_type

    @property
    def upgrade_cost(self) -> str:
        return self.__upgrade_cost

    @property
    def unlock_cost(self) -> str:
        return self.__unlock_cost

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def visibility_flags(self) -> str:
        return self.__visibility_flags

    @property
    def unlock_from_ship_design_id(self) -> int:
        return self.__unlock_from_ship_design_id

    @property
    def required_research_design_id(self) -> int:
        return self.__required_research_design_id

    @property
    def thrust_particle_sprite_id(self) -> int:
        return self.__thrust_particle_sprite_id

    @property
    def thrust_line_animation_id(self) -> int:
        return self.__thrust_line_animation_id

    @property
    def required_ship_design_id(self) -> int:
        return self.__required_ship_design_id

    @property
    def race_id(self) -> int:
        return self.__race_id

    @property
    def exterior_file_id(self) -> int:
        return self.__exterior_file_id

    @property
    def interior_file_id(self) -> int:
        return self.__interior_file_id

    @property
    def logo_file_id(self) -> int:
        return self.__logo_file_id

    @property
    def room_frame_file_id(self) -> int:
        return self.__room_frame_file_id

    @property
    def lift_file_id(self) -> int:
        return self.__lift_file_id

    @property
    def door_frame_left_file_id(self) -> int:
        return self.__door_frame_left_file_id

    @property
    def door_frame_right_file_id(self) -> int:
        return self.__door_frame_right_file_id

    @property
    def foreground_asset_id(self) -> int:
        return self.__foreground_asset_id

    @property
    def background_asset_id(self) -> int:
        return self.__background_asset_id
