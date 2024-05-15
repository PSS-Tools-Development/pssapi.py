from typing import Union

from .. import enums
from ..types import EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase
from .metadata import RoomDesignMetadata
from .raw import RoomDesignRaw
from . import properties


class RoomDesign(RoomDesignRaw, EntityWithIdBase):
    def __init__(self, room_design_info: EntityInfo) -> None:
        super().__init__(room_design_info)
        self._category_type_enum: enums.CategoryType = _parse.pss_str_enum(self.category_type, enums.CategoryType)
        self._enhancement_type_enum: enums.EnhancementType = _parse.pss_str_enum(self.enhancement_type, enums.EnhancementType)
        self._flags_enum: enums.RoomFlags = _parse.pss_int_flag(self.flags, enums.RoomFlags)
        self._manufacture_type_enum: enums.ManufactureType = _parse.pss_str_enum(self.manufacture_type, enums.ManufactureType)
        self._room_design_metadata: RoomDesignMetadata = RoomDesignMetadata(self.metadata)
        self._room_type_enum: enums.RoomType = _parse.pss_str_enum(self.room_type, enums.RoomType)
        self._supported_grid_types_enum: enums.GridTypeFlag = _parse.pss_int_flag(self.supported_grid_types, enums.GridTypeFlag)
        self._target_type_enum: enums.TargetType = _parse.pss_str_enum(self.target_type, enums.TargetType)

        self._room_type_properties: properties.RoomTypeProperties = properties.RoomTypeProperties(self)

    @property
    def id(self) -> int:
        return self.room_design_id

    @property
    def category_type_enum(self) -> "enums.CategoryType":
        return self._category_type_enum

    @property
    def enhancement_type_enum(self) -> "enums.EnhancementType":
        return self._enhancement_type_enum

    @property
    def flags_enum(self) -> "enums.RoomFlags":
        return self._flags_enum

    @property
    def manufacture_type_enum(self) -> "enums.ManufactureType":
        return self._manufacture_type_enum

    @property
    def room_design_metadata(self) -> RoomDesignMetadata:
        return self._room_design_metadata

    @property
    def room_type_enum(self) -> "enums.RoomType":
        return self._room_type_enum

    @property
    def room_type_properties(self) -> "properties.RoomTypeProperties":
        return self._room_type_properties

    @property
    def supported_grid_types_enum(self) -> "enums.GridTypeFlag":
        return self._supported_grid_types_enum

    @property
    def target_type_enum(self) -> "enums.TargetType":
        return self._target_type_enum

    def get_room_type_properties(
        self,
    ) -> Union[
        "properties.AndroidRoomProperties",
        "properties.AntiCraftProperties",
        "properties.BedroomRoomProperties",
        "properties.BridgeRoomProperties",
        "properties.CannonRoomProperties",
        "properties.CarrierRoomProperties",
        "properties.CommandRoomProperties",
        "properties.CorridorRoomProperties",
        "properties.CouncilRoomProperties",
        "properties.EngineRoomProperties",
        "properties.HullRoomProperties",
        "properties.LaserRoomProperties",
        "properties.LiftRoomProperties",
        "properties.MedicalRoomProperties",
        "properties.MissileRoomProperties",
        "properties.PrinterRoomProperties",
        "properties.RadarRoomProperties",
        "properties.ReactorRoomProperties",
        "properties.RecyclingRoomProperties",
        "properties.ResearchRoomProperties",
        "properties.ResourceRoomProperties",
        "properties.ShieldRoomProperties",
        "properties.StationMissileRoomProperties",
        "properties.StealthRoomProperties",
        "properties.StorageRoomProperties",
        "properties.SuperWeaponRoomProperties",
        "properties.TeleportRoomProperties",
        "properties.TrainingRoomProperties",
        "properties.TrapRoomProperties",
        "properties.WallRoomProperties",
    ]:
        """
        Short for `self.room_type_properties.get_room_type_properties()`
        """
        return self.room_type_properties.get_room_type_properties()
