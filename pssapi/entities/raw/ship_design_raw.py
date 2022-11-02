"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ShipDesignRaw:
    XML_NODE_NAME: str = 'ShipDesign'

    def __init__(self, ship_design_info: _EntityInfo) -> None:
        self.__columns: int = _parse.pss_int(ship_design_info.get('Columns'))
        self.__race_id: int = _parse.pss_int(ship_design_info.get('RaceId'))
        self.__logo_sprite_id: int = _parse.pss_int(
            ship_design_info.get('LogoSpriteId'))
        self.__required_research_design_id: int = _parse.pss_int(
            ship_design_info.get('RequiredResearchDesignId'))
        self.__engine_y: int = _parse.pss_int(ship_design_info.get('EngineY'))
        self.__flag_y: int = _parse.pss_int(ship_design_info.get('FlagY'))
        self.__upgrade_time: int = _parse.pss_int(
            ship_design_info.get('UpgradeTime'))
        self.__interior_sprite_id: int = _parse.pss_int(
            ship_design_info.get('InteriorSpriteId'))
        self.__ship_description: str = _parse.pss_str(
            ship_design_info.get('ShipDescription'))
        self.__lift_file_id: int = _parse.pss_int(
            ship_design_info.get('LiftFileId'))
        self.__door_frame_right_file_id: int = _parse.pss_int(
            ship_design_info.get('DoorFrameRightFileId'))
        self.__interior_file_id: int = _parse.pss_int(
            ship_design_info.get('InteriorFileId'))
        self.__mini_ship_sprite_id: int = _parse.pss_int(
            ship_design_info.get('MiniShipSpriteId'))
        self.__room_frame_sprite_id: int = _parse.pss_int(
            ship_design_info.get('RoomFrameSpriteId'))
        self.__mask: str = _parse.pss_str(ship_design_info.get('Mask'))
        self.__door_frame_right_sprite_id: int = _parse.pss_int(
            ship_design_info.get('DoorFrameRightSpriteId'))
        self.__background_asset_id: int = _parse.pss_int(
            ship_design_info.get('BackgroundAssetId'))
        self.__requirement_string: str = _parse.pss_str(
            ship_design_info.get('RequirementString'))
        self.__gas_capacity: int = _parse.pss_int(
            ship_design_info.get('GasCapacity'))
        self.__foreground_asset_id: int = _parse.pss_int(
            ship_design_info.get('ForegroundAssetId'))
        self.__upgrade_cost: str = _parse.pss_str(
            ship_design_info.get('UpgradeCost'))
        self.__logo_file_id: int = _parse.pss_int(
            ship_design_info.get('LogoFileId'))
        self.__equipment_capacity: int = _parse.pss_int(
            ship_design_info.get('EquipmentCapacity'))
        self.__flag_x: int = _parse.pss_int(ship_design_info.get('FlagX'))
        self.__ship_design_id: int = _parse.pss_int(
            ship_design_info.get('ShipDesignId'))
        self.__exterior_file_id: int = _parse.pss_int(
            ship_design_info.get('ExteriorFileId'))
        self.__hp: int = _parse.pss_int(ship_design_info.get('Hp'))
        self.__ship_design_name: str = _parse.pss_str(
            ship_design_info.get('ShipDesignName'))
        self.__visibility_flags: str = _parse.pss_str(
            ship_design_info.get('VisibilityFlags'))
        self.__repair_time: int = _parse.pss_int(
            ship_design_info.get('RepairTime'))
        self.__upgrade_offset_rows: int = _parse.pss_int(
            ship_design_info.get('UpgradeOffsetRows'))
        self.__thrust_particle_sprite_id: int = _parse.pss_int(
            ship_design_info.get('ThrustParticleSpriteId'))
        self.__ship_type: str = _parse.pss_str(
            ship_design_info.get('ShipType'))
        self.__ship_level: int = _parse.pss_int(
            ship_design_info.get('ShipLevel'))
        self.__upgrade_offset_columns: int = _parse.pss_int(
            ship_design_info.get('UpgradeOffsetColumns'))
        self.__exterior_sprite_id: int = _parse.pss_int(
            ship_design_info.get('ExteriorSpriteId'))
        self.__unlock_from_ship_design_id: int = _parse.pss_int(
            ship_design_info.get('UnlockFromShipDesignId'))
        self.__allow_interacial: bool = _parse.pss_bool(
            ship_design_info.get('AllowInteracial'))
        self.__unlock_cost: str = _parse.pss_str(
            ship_design_info.get('UnlockCost'))
        self.__required_ship_design_id: int = _parse.pss_int(
            ship_design_info.get('RequiredShipDesignId'))
        self.__mineral_cost: int = _parse.pss_int(
            ship_design_info.get('MineralCost'))
        self.__door_frame_left_file_id: int = _parse.pss_int(
            ship_design_info.get('DoorFrameLeftFileId'))
        self.__rows: int = _parse.pss_int(ship_design_info.get('Rows'))
        self.__thrust_line_animation_id: int = _parse.pss_int(
            ship_design_info.get('ThrustLineAnimationId'))
        self.__door_frame_left_sprite_id: int = _parse.pss_int(
            ship_design_info.get('DoorFrameLeftSpriteId'))
        self.__room_frame_file_id: int = _parse.pss_int(
            ship_design_info.get('RoomFrameFileId'))
        self.__starbux_cost: int = _parse.pss_int(
            ship_design_info.get('StarbuxCost'))
        self.__thrust_scale: float = _parse.pss_float(
            ship_design_info.get('ThrustScale'))
        self.__mineral_capacity: int = _parse.pss_int(
            ship_design_info.get('MineralCapacity'))
        self.__engine_x: int = _parse.pss_int(ship_design_info.get('EngineX'))
        self.__lift_sprite_id: int = _parse.pss_int(
            ship_design_info.get('LiftSpriteId'))

    @property
    def columns(self) -> int:
        return self.__columns

    @property
    def race_id(self) -> int:
        return self.__race_id

    @property
    def logo_sprite_id(self) -> int:
        return self.__logo_sprite_id

    @property
    def required_research_design_id(self) -> int:
        return self.__required_research_design_id

    @property
    def engine_y(self) -> int:
        return self.__engine_y

    @property
    def flag_y(self) -> int:
        return self.__flag_y

    @property
    def upgrade_time(self) -> int:
        return self.__upgrade_time

    @property
    def interior_sprite_id(self) -> int:
        return self.__interior_sprite_id

    @property
    def ship_description(self) -> str:
        return self.__ship_description

    @property
    def lift_file_id(self) -> int:
        return self.__lift_file_id

    @property
    def door_frame_right_file_id(self) -> int:
        return self.__door_frame_right_file_id

    @property
    def interior_file_id(self) -> int:
        return self.__interior_file_id

    @property
    def mini_ship_sprite_id(self) -> int:
        return self.__mini_ship_sprite_id

    @property
    def room_frame_sprite_id(self) -> int:
        return self.__room_frame_sprite_id

    @property
    def mask(self) -> str:
        return self.__mask

    @property
    def door_frame_right_sprite_id(self) -> int:
        return self.__door_frame_right_sprite_id

    @property
    def background_asset_id(self) -> int:
        return self.__background_asset_id

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def gas_capacity(self) -> int:
        return self.__gas_capacity

    @property
    def foreground_asset_id(self) -> int:
        return self.__foreground_asset_id

    @property
    def upgrade_cost(self) -> str:
        return self.__upgrade_cost

    @property
    def logo_file_id(self) -> int:
        return self.__logo_file_id

    @property
    def equipment_capacity(self) -> int:
        return self.__equipment_capacity

    @property
    def flag_x(self) -> int:
        return self.__flag_x

    @property
    def ship_design_id(self) -> int:
        return self.__ship_design_id

    @property
    def exterior_file_id(self) -> int:
        return self.__exterior_file_id

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def ship_design_name(self) -> str:
        return self.__ship_design_name

    @property
    def visibility_flags(self) -> str:
        return self.__visibility_flags

    @property
    def repair_time(self) -> int:
        return self.__repair_time

    @property
    def upgrade_offset_rows(self) -> int:
        return self.__upgrade_offset_rows

    @property
    def thrust_particle_sprite_id(self) -> int:
        return self.__thrust_particle_sprite_id

    @property
    def ship_type(self) -> str:
        return self.__ship_type

    @property
    def ship_level(self) -> int:
        return self.__ship_level

    @property
    def upgrade_offset_columns(self) -> int:
        return self.__upgrade_offset_columns

    @property
    def exterior_sprite_id(self) -> int:
        return self.__exterior_sprite_id

    @property
    def unlock_from_ship_design_id(self) -> int:
        return self.__unlock_from_ship_design_id

    @property
    def allow_interacial(self) -> bool:
        return self.__allow_interacial

    @property
    def unlock_cost(self) -> str:
        return self.__unlock_cost

    @property
    def required_ship_design_id(self) -> int:
        return self.__required_ship_design_id

    @property
    def mineral_cost(self) -> int:
        return self.__mineral_cost

    @property
    def door_frame_left_file_id(self) -> int:
        return self.__door_frame_left_file_id

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def thrust_line_animation_id(self) -> int:
        return self.__thrust_line_animation_id

    @property
    def door_frame_left_sprite_id(self) -> int:
        return self.__door_frame_left_sprite_id

    @property
    def room_frame_file_id(self) -> int:
        return self.__room_frame_file_id

    @property
    def starbux_cost(self) -> int:
        return self.__starbux_cost

    @property
    def thrust_scale(self) -> float:
        return self.__thrust_scale

    @property
    def mineral_capacity(self) -> int:
        return self.__mineral_capacity

    @property
    def engine_x(self) -> int:
        return self.__engine_x

    @property
    def lift_sprite_id(self) -> int:
        return self.__lift_sprite_id
