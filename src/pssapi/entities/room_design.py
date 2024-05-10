from typing import Union as _Union

from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import RoomDesignMetadata as _RoomDesignMetadata
from .raw import RoomDesignRaw as _RoomDesignRaw


class RoomDesign(_RoomDesignRaw, _EntityWithIdBase):
    def __init__(self, room_design_info: _EntityInfo) -> None:
        super().__init__(room_design_info)
        self._category_type_enum: _enums.CategoryType = _parse.pss_str_enum(self.category_type, _enums.CategoryType)
        self._enhancement_type_enum: _enums.EnhancementType = _parse.pss_str_enum(self.enhancement_type, _enums.EnhancementType)
        self._flags_enum: _enums.RoomFlags = _parse.pss_int_flag(self.flags, _enums.RoomFlags)
        self._manufacture_type_enum: _enums.ManufactureType = _parse.pss_str_enum(self.manufacture_type, _enums.ManufactureType)
        self._room_design_metadata: _RoomDesignMetadata = _RoomDesignMetadata(self.metadata)
        self._room_type_enum: _enums.RoomType = _parse.pss_str_enum(self.room_type, _enums.RoomType)
        self._supported_grid_types_enum: _enums.GridTypeFlag = _parse.pss_int_flag(self.supported_grid_types, _enums.GridTypeFlag)
        self._target_type_enum: _enums.TargetType = _parse.pss_str_enum(self.target_type, _enums.TargetType)
        self._room_type_properties: RoomTypeProperties = RoomTypeProperties(self)

    @property
    def id(self) -> int:
        return self.room_design_id

    @property
    def category_type_enum(self) -> "_enums.CategoryType":
        return self._category_type_enum

    @property
    def enhancement_type_enum(self) -> "_enums.EnhancementType":
        return self._enhancement_type_enum

    @property
    def flags_enum(self) -> "_enums.RoomFlags":
        return self._flags_enum

    @property
    def manufacture_type_enum(self) -> "_enums.ManufactureType":
        return self._manufacture_type_enum

    @property
    def room_design_metadata(self) -> _RoomDesignMetadata:
        return self._room_design_metadata

    @property
    def room_type_enum(self) -> "_enums.RoomType":
        return self._room_type_enum

    @property
    def room_type_properties(self) -> "RoomTypeProperties":
        return self._room_type_properties

    @property
    def supported_grid_types_enum(self) -> "_enums.GridTypeFlag":
        return self._supported_grid_types_enum

    @property
    def target_type_enum(self) -> "_enums.TargetType":
        return self._target_type_enum

    def get_room_type_properties(
        self,
    ) -> _Union[
        "AndroidRoomProperties",
        "AntiCraftProperties",
        "BedroomRoomProperties",
        "BridgeRoomProperties",
        "CannonRoomProperties",
        "CarrierRoomProperties",
        "CommandRoomProperties",
        "CorridorRoomProperties",
        "CouncilRoomProperties",
        "EngineRoomProperties",
        "HullRoomProperties",
        "LaserRoomProperties",
        "LiftRoomProperties",
        "MedicalRoomProperties",
        "MissileRoomProperties",
        "PrinterRoomProperties",
        "RadarRoomProperties",
        "ReactorRoomProperties",
        "RecyclingRoomProperties",
        "ResearchRoomProperties",
        "ResourceRoomProperties",
        "ShieldRoomProperties",
        "StationMissileRoomProperties",
        "StealthRoomProperties",
        "StorageRoomProperties",
        "SuperWeaponRoomProperties",
        "TeleportRoomProperties",
        "TrainingRoomProperties",
        "TrapRoomProperties",
        "WallRoomProperties",
    ]:
        """
        Short for `self.room_type_properties.get_room_type_properties()`
        """
        return self.room_type_properties.get_room_type_properties()


class RoomTypeProperties:
    def __init__(self, room_design: RoomDesign):
        self._room_design: RoomDesign = room_design

        self._android_room_properties: AndroidRoomProperties = None
        self._anticraft_room_properties: AntiCraftProperties = None
        self._bedroom_room_properties: BedroomRoomProperties = None
        self._bridge_room_properties: BridgeRoomProperties = None
        self._cannon_room_properties: CannonRoomProperties = None
        self._carrier_room_properties: CarrierRoomProperties = None
        self._command_room_properties: CommandRoomProperties = None
        self._corridor_room_properties: CorridorRoomProperties = None
        self._council_room_properties: CouncilRoomProperties = None
        self._engine_room_properties: EngineRoomProperties = None
        self._hull_room_properties: HullRoomProperties = None
        self._laser_room_properties: LaserRoomProperties = None
        self._lift_room_properties: LiftRoomProperties = None
        self._medical_room_properties: MedicalRoomProperties = None
        self._missile_room_properties: MissileRoomProperties = None
        self._printer_room_properties: PrinterRoomProperties = None
        self._radar_room_properties: RadarRoomProperties = None
        self._reactor_room_properties: ReactorRoomProperties = None
        self._recycling_room_properties: RecyclingRoomProperties = None
        self._research_room_properties: ResearchRoomProperties = None
        self._resource_room_properties: ResearchRoomProperties = None
        self._shield_room_properties: ShieldRoomProperties = None
        self._station_missile_properties: StationMissileRoomProperties = None
        self._stealth_room_properties: StealthRoomProperties = None
        self._storage_room_properties: StorageRoomProperties = None
        self._super_weapon_room_properties: SuperWeaponRoomProperties = None
        self._teleport_room_properties: TeleportRoomProperties = None
        self._training_room_properties: TrainingRoomProperties = None
        self._trap_room_properties: TrapRoomProperties = None
        self._wall_room_properties: WallRoomProperties = None

    @property
    def android_room_properties(self) -> "AndroidRoomProperties":
        if self._android_room_properties is None:
            self._android_room_properties = AndroidRoomProperties(self._room_design)
        return self._android_room_properties

    @property
    def anticraft_room_properties(self) -> "AntiCraftProperties":
        if self._anticraft_room_properties is None:
            self._anticraft_room_properties = AntiCraftProperties(self._room_design)
        return self._anticraft_room_properties

    @property
    def bedroom_room_properties(self) -> "BedroomRoomProperties":
        if self._bedroom_room_properties is None:
            self._bedroom_room_properties = BedroomRoomProperties(self._room_design)
        return self._bedroom_room_properties

    @property
    def bridge_room_properties(self) -> "BridgeRoomProperties":
        if self._bridge_room_properties is None:
            self._bridge_room_properties = BridgeRoomProperties(self._room_design)
        return self._bridge_room_properties

    @property
    def cannon_room_properties(self) -> "CannonRoomProperties":
        if self._cannon_room_properties is None:
            self._cannon_room_properties = CannonRoomProperties(self._room_design)
        return self._cannon_room_properties

    @property
    def carrier_room_properties(self) -> "CarrierRoomProperties":
        if self._carrier_room_properties is None:
            self._carrier_room_properties = CarrierRoomProperties(self._room_design)
        return self._carrier_room_properties

    @property
    def command_room_properties(self) -> "CommandRoomProperties":
        if self._command_room_properties is None:
            self._command_room_properties = CommandRoomProperties(self._room_design)
        return self._command_room_properties

    @property
    def corridor_room_properties(self) -> "CorridorRoomProperties":
        if self._corridor_room_properties is None:
            self._corridor_room_properties = CorridorRoomProperties(self._room_design)
        return self._corridor_room_properties

    @property
    def council_room_properties(self) -> "CouncilRoomProperties":
        if self._council_room_properties is None:
            self._council_room_properties = CouncilRoomProperties(self._room_design)
        return self._council_room_properties

    @property
    def engine_room_properties(self) -> "EngineRoomProperties":
        if self._engine_room_properties is None:
            self._engine_room_properties = EngineRoomProperties(self._room_design)
        return self._engine_room_properties

    @property
    def hull_room_properties(self) -> "HullRoomProperties":
        if self._hull_room_properties is None:
            self._hull_room_properties = HullRoomProperties(self._room_design)
        return self._hull_room_properties

    @property
    def laser_room_properties(self) -> "LaserRoomProperties":
        if self._laser_room_properties is None:
            self._laser_room_properties = LaserRoomProperties(self._room_design)
        return self._laser_room_properties

    @property
    def lift_room_properties(self) -> "LiftRoomProperties":
        if self._lift_room_properties is None:
            self._lift_room_properties = LiftRoomProperties(self._room_design)
        return self._lift_room_properties

    @property
    def medical_room_properties(self) -> "MedicalRoomProperties":
        if self._medical_room_properties is None:
            self._medical_room_properties = MedicalRoomProperties(self._room_design)
        return self._medical_room_properties

    @property
    def missile_room_properties(self) -> "MissileRoomProperties":
        if self._missile_room_properties is None:
            self._missile_room_properties = MissileRoomProperties(self._room_design)
        return self._missile_room_properties

    @property
    def printer_room_properties(self) -> "PrinterRoomProperties":
        if self._printer_room_properties is None:
            self._printer_room_properties = PrinterRoomProperties(self._room_design)
        return self._printer_room_properties

    @property
    def radar_room_properties(self) -> "RadarRoomProperties":
        if self._radar_room_properties is None:
            self._radar_room_properties = RadarRoomProperties(self._room_design)
        return self._radar_room_properties

    @property
    def reactor_room_properties(self) -> "ReactorRoomProperties":
        if self._reactor_room_properties is None:
            self._reactor_room_properties = ReactorRoomProperties(self._room_design)
        return self._reactor_room_properties

    @property
    def recycling_room_properties(self) -> "RecyclingRoomProperties":
        if self._recycling_room_properties is None:
            self._recycling_room_properties = RecyclingRoomProperties(self._room_design)
        return self._recycling_room_properties

    @property
    def research_room_properties(self) -> "ResearchRoomProperties":
        if self._research_room_properties is None:
            self._research_room_properties = ResearchRoomProperties(self._room_design)
        return self._research_room_properties

    @property
    def resource_room_properties(self) -> "ResearchRoomProperties":
        if self._resource_room_properties is None:
            self._resource_room_properties = ResearchRoomProperties(self._room_design)
        return self._resource_room_properties

    @property
    def shield_room_properties(self) -> "ShieldRoomProperties":
        if self._shield_room_properties is None:
            self._shield_room_properties = ShieldRoomProperties(self._room_design)
        return self._shield_room_properties

    @property
    def station_missile_properties(self) -> "StationMissileRoomProperties":
        if self._station_missile_properties is None:
            self._station_missile_properties = StationMissileRoomProperties(self._room_design)
        return self._station_missile_properties

    @property
    def stealth_room_properties(self) -> "StealthRoomProperties":
        if self._stealth_room_properties is None:
            self._stealth_room_properties = StealthRoomProperties(self._room_design)
        return self._stealth_room_properties

    @property
    def storage_room_properties(self) -> "StorageRoomProperties":
        if self._storage_room_properties is None:
            self._storage_room_properties = StorageRoomProperties(self._room_design)
        return self._storage_room_properties

    @property
    def super_weapon_room_properties(self) -> "SuperWeaponRoomProperties":
        if self._super_weapon_room_properties is None:
            self._super_weapon_room_properties = SuperWeaponRoomProperties(self._room_design)
        return self._super_weapon_room_properties

    @property
    def teleport_room_properties(self) -> "TeleportRoomProperties":
        if self._teleport_room_properties is None:
            self._teleport_room_properties = TeleportRoomProperties(self._room_design)
        return self._teleport_room_properties

    @property
    def training_room_properties(self) -> "TrainingRoomProperties":
        if self._training_room_properties is None:
            self._training_room_properties = TrainingRoomProperties(self._room_design)
        return self._training_room_properties

    @property
    def trap_room_properties(self) -> "TrapRoomProperties":
        if self._trap_room_properties is None:
            self._trap_room_properties = TrapRoomProperties(self._room_design)
        return self._trap_room_properties

    @property
    def wall_room_properties(self) -> "WallRoomProperties":
        if self._wall_room_properties is None:
            self._wall_room_properties = WallRoomProperties(self._room_design)
        return self._wall_room_properties

    def get_room_type_properties(
        self,
    ) -> _Union[
        "AndroidRoomProperties",
        "AntiCraftProperties",
        "BedroomRoomProperties",
        "BridgeRoomProperties",
        "CannonRoomProperties",
        "CarrierRoomProperties",
        "CommandRoomProperties",
        "CorridorRoomProperties",
        "CouncilRoomProperties",
        "EngineRoomProperties",
        "HullRoomProperties",
        "LaserRoomProperties",
        "LiftRoomProperties",
        "MedicalRoomProperties",
        "MissileRoomProperties",
        "PrinterRoomProperties",
        "RadarRoomProperties",
        "ReactorRoomProperties",
        "RecyclingRoomProperties",
        "ResearchRoomProperties",
        "ResourceRoomProperties",
        "ShieldRoomProperties",
        "StationMissileRoomProperties",
        "StealthRoomProperties",
        "StorageRoomProperties",
        "SuperWeaponRoomProperties",
        "TeleportRoomProperties",
        "TrainingRoomProperties",
        "TrapRoomProperties",
        "WallRoomProperties",
    ]:
        return get_room_properties(self._room_design, self._room_design.room_type_enum)


class _RoomPropertiesBase:
    def __init__(self, room_design: RoomDesign):
        self._room_design: RoomDesign = room_design


class AndroidRoomProperties(_RoomPropertiesBase):
    @property
    def deploy_limit(self) -> int:
        return self._room_design.range
    
    @property
    def queue_limit(self) -> int:
        return self._room_design.manufacture_capacity
    
    @property
    def storage_limit(self) -> int:
        return self._room_design.capacity


class AntiCraftProperties(_RoomPropertiesBase):
    pass


class BedroomRoomProperties(_RoomPropertiesBase):
    pass


class BridgeRoomProperties(_RoomPropertiesBase):
    pass


class CannonRoomProperties(_RoomPropertiesBase):
    pass


class CarrierRoomProperties(_RoomPropertiesBase):
    pass


class CommandRoomProperties(_RoomPropertiesBase):
    pass


class CorridorRoomProperties(_RoomPropertiesBase):
    pass


class CouncilRoomProperties(_RoomPropertiesBase):
    pass


class EngineRoomProperties(_RoomPropertiesBase):
    pass


class HullRoomProperties(_RoomPropertiesBase):
    pass


class LaserRoomProperties(_RoomPropertiesBase):
    pass


class LiftRoomProperties(_RoomPropertiesBase):
    pass


class MedicalRoomProperties(_RoomPropertiesBase):
    pass


class MissileRoomProperties(_RoomPropertiesBase):
    pass


class PrinterRoomProperties(_RoomPropertiesBase):
    pass


class RadarRoomProperties(_RoomPropertiesBase):
    pass


class ReactorRoomProperties(_RoomPropertiesBase):
    pass


class RecyclingRoomProperties(_RoomPropertiesBase):
    @property
    def gas_per_crew(self) -> int:
        """
        Gas collected per crew that died in battle.
        """
        return self._room_design.manufacture_rate

    @property
    def max_crew_blend(self) -> int:
        """
        Maximum number of crews the player can blend, before an item has to be crafted.
        """
        return self._room_design.manufacture_capacity

    @property
    def max_storage(self) -> int:
        """
        The maximum DNA that can be stored.
        """
        return self._room_design.capacity


class ResearchRoomProperties(_RoomPropertiesBase):
    pass


class ResourceRoomProperties(_RoomPropertiesBase):
    pass


class ShieldRoomProperties(_RoomPropertiesBase):
    def __init__(self, room_design: RoomDesign):
        super().__init__(room_design)
        self._shield_restored_on_reload: float = None

    @property
    def shield_hp(self) -> int:
        """
        Amount of shield HP added to maximum shield HP.
        """
        return self._room_design.capacity

    @property
    def restore_on_reload(self) -> float:
        """
        Amount of shield HP added, when the room reloads.
        """
        if self._shield_restored_on_reload is None:
            self._shield_restored_on_reload = self._room_design.manufacture_capacity / 100.0
        return self._shield_restored_on_reload


class StationMissileRoomProperties(_RoomPropertiesBase):
    pass


class StealthRoomProperties(_RoomPropertiesBase):
    pass


class StorageRoomProperties(_RoomPropertiesBase):
    pass


class SuperWeaponRoomProperties(_RoomPropertiesBase):
    pass


class TeleportRoomProperties(_RoomPropertiesBase):
    pass


class TrainingRoomProperties(_RoomPropertiesBase):
    pass


class TrapRoomProperties(_RoomPropertiesBase):
    pass


class WallRoomProperties(_RoomPropertiesBase):
    pass


def get_room_properties(
    room_design: RoomDesign, room_type: "_enums.RoomType"
) -> _Union[
    "AndroidRoomProperties",
    "AntiCraftProperties",
    "BedroomRoomProperties",
    "BridgeRoomProperties",
    "CannonRoomProperties",
    "CarrierRoomProperties",
    "CommandRoomProperties",
    "CorridorRoomProperties",
    "CouncilRoomProperties",
    "EngineRoomProperties",
    "HullRoomProperties",
    "LaserRoomProperties",
    "LiftRoomProperties",
    "MedicalRoomProperties",
    "MissileRoomProperties",
    "PrinterRoomProperties",
    "RadarRoomProperties",
    "ReactorRoomProperties",
    "RecyclingRoomProperties",
    "ResearchRoomProperties",
    "ResourceRoomProperties",
    "ShieldRoomProperties",
    "StationMissileRoomProperties",
    "StealthRoomProperties",
    "StorageRoomProperties",
    "SuperWeaponRoomProperties",
    "TeleportRoomProperties",
    "TrainingRoomProperties",
    "TrapRoomProperties",
    "WallRoomProperties",
]:
    if room_type == _enums.RoomType.ANDROID:
        return room_design.room_type_properties.android_room_properties
    if room_type == _enums.RoomType.ANTI_CRAFT:
        return room_design.room_type_properties.anticraft_room_properties
    if room_type == _enums.RoomType.BEDROOM:
        return room_design.room_type_properties.bedroom_room_properties
    if room_type == _enums.RoomType.BRIDGE:
        return room_design.room_type_properties.bridge_room_properties
    if room_type == _enums.RoomType.CANNON:
        return room_design.room_type_properties.cannon_room_properties
    if room_type == _enums.RoomType.CARRIER:
        return room_design.room_type_properties.carrier_room_properties
    if room_type == _enums.RoomType.COMMAND:
        return room_design.room_type_properties.command_room_properties
    if room_type == _enums.RoomType.CORRIDOR:
        return room_design.room_type_properties.corridor_room_properties
    if room_type == _enums.RoomType.COUNCIL:
        return room_design.room_type_properties.council_room_properties
    if room_type == _enums.RoomType.ENGINE:
        return room_design.room_type_properties.engine_room_properties
    if room_type == _enums.RoomType.GAS:
        return room_design.room_type_properties.resource_room_properties
    if room_type == _enums.RoomType.HULL:
        return room_design.room_type_properties.hull_room_properties
    if room_type == _enums.RoomType.LASER:
        return room_design.room_type_properties.laser_room_properties
    if room_type == _enums.RoomType.LIFT:
        return room_design.room_type_properties.lift_room_properties
    if room_type == _enums.RoomType.MEDICAL:
        return room_design.room_type_properties.medical_room_properties
    if room_type == _enums.RoomType.MINERAL:
        return room_design.room_type_properties.resource_room_properties
    if room_type == _enums.RoomType.PRINTER:
        return room_design.room_type_properties.printer_room_properties
    if room_type == _enums.RoomType.RADAR:
        return room_design.room_type_properties.radar_room_properties
    if room_type == _enums.RoomType.REACTOR:
        return room_design.room_type_properties.reactor_room_properties
    if room_type == _enums.RoomType.RECYCLING:
        return room_design.room_type_properties.recycling_room_properties
    if room_type == _enums.RoomType.RESEARCH:
        return room_design.room_type_properties.research_room_properties
    if room_type == _enums.RoomType.SHIELD:
        return room_design.room_type_properties.shield_room_properties
    if room_type == _enums.RoomType.STATION_MISSILE:
        return room_design.room_type_properties.station_missile_properties
    if room_type == _enums.RoomType.STEALTH:
        return room_design.room_type_properties.stealth_room_properties
    if room_type == _enums.RoomType.STORAGE:
        return room_design.room_type_properties.storage_room_properties
    if room_type == _enums.RoomType.SUPER_WEAPON:
        return room_design.room_type_properties.super_weapon_room_properties
    if room_type == _enums.RoomType.SUPPLY:
        return room_design.room_type_properties.resource_room_properties
    if room_type == _enums.RoomType.TELEPORT:
        return room_design.room_type_properties.teleport_room_properties
    if room_type == _enums.RoomType.TRAINING:
        return room_design.room_type_properties.training_room_properties
    if room_type == _enums.RoomType.TRAP:
        return room_design.room_type_properties.trap_room_properties
    if room_type == _enums.RoomType.WALL:
        return room_design.room_type_properties.wall_room_properties
    return None
