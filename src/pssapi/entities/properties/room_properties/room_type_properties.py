from typing import Union

from .... import entities, enums
from .android_room_properties import AndroidRoomProperties
from .anticraft_room_properties import AntiCraftProperties
from .bedroom_room_properties import BedroomRoomProperties
from .bridge_room_properties import BridgeRoomProperties
from .cannon_room_properties import CannonRoomProperties
from .carrier_room_properties import CarrierRoomProperties
from .command_room_properties import CommandRoomProperties
from .corridor_room_properties import CorridorRoomProperties
from .council_room_properties import CouncilRoomProperties
from .engine_room_properties import EngineRoomProperties
from .hull_room_properties import HullRoomProperties
from .laser_room_properties import LaserRoomProperties
from .lift_room_properties import LiftRoomProperties
from .medical_room_properties import MedicalRoomProperties
from .missile_room_properties import MissileRoomProperties
from .printer_room_properties import PrinterRoomProperties
from .radar_room_properties import RadarRoomProperties
from .reactor_room_properties import ReactorRoomProperties
from .recycling_room_properties import RecyclingRoomProperties
from .research_room_properties import ResearchRoomProperties
from .resource_room_properties import ResourceRoomProperties
from .shield_room_properties import ShieldRoomProperties
from .station_missile_properties import StationMissileRoomProperties
from .stealth_room_properties import StealthRoomProperties
from .storage_room_properties import StorageRoomProperties
from .super_weapon_room_properties import SuperWeaponRoomProperties
from .teleport_room_properties import TeleportRoomProperties
from .training_room_properties import TrainingRoomProperties
from .trap_room_properties import TrapRoomProperties
from .wall_room_properties import WallRoomProperties


class RoomTypeProperties:
    def __init__(self, room_design: "entities.RoomDesign"):
        self._room_design: entities.RoomDesign = room_design

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
    def resource_room_properties(self) -> "ResourceRoomProperties":
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
    ) -> Union[
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
        return get_room_properties_by_type(self._room_design, self._room_design.room_type_enum)


def get_room_properties_by_type(
    room_design: "entities.RoomDesign", room_type: "enums.RoomType"
) -> Union[
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
    if room_type == enums.RoomType.ANDROID:
        return room_design.room_type_properties.android_room_properties
    if room_type == enums.RoomType.ANTI_CRAFT:
        return room_design.room_type_properties.anticraft_room_properties
    if room_type == enums.RoomType.BEDROOM:
        return room_design.room_type_properties.bedroom_room_properties
    if room_type == enums.RoomType.BRIDGE:
        return room_design.room_type_properties.bridge_room_properties
    if room_type == enums.RoomType.CANNON:
        return room_design.room_type_properties.cannon_room_properties
    if room_type == enums.RoomType.CARRIER:
        return room_design.room_type_properties.carrier_room_properties
    if room_type == enums.RoomType.COMMAND:
        return room_design.room_type_properties.command_room_properties
    if room_type == enums.RoomType.CORRIDOR:
        return room_design.room_type_properties.corridor_room_properties
    if room_type == enums.RoomType.COUNCIL:
        return room_design.room_type_properties.council_room_properties
    if room_type == enums.RoomType.ENGINE:
        return room_design.room_type_properties.engine_room_properties
    if room_type == enums.RoomType.GAS:
        return room_design.room_type_properties.resource_room_properties
    if room_type == enums.RoomType.HULL:
        return room_design.room_type_properties.hull_room_properties
    if room_type == enums.RoomType.LASER:
        return room_design.room_type_properties.laser_room_properties
    if room_type == enums.RoomType.LIFT:
        return room_design.room_type_properties.lift_room_properties
    if room_type == enums.RoomType.MEDICAL:
        return room_design.room_type_properties.medical_room_properties
    if room_type == enums.RoomType.MINERAL:
        return room_design.room_type_properties.resource_room_properties
    if room_type == enums.RoomType.PRINTER:
        return room_design.room_type_properties.printer_room_properties
    if room_type == enums.RoomType.RADAR:
        return room_design.room_type_properties.radar_room_properties
    if room_type == enums.RoomType.REACTOR:
        return room_design.room_type_properties.reactor_room_properties
    if room_type == enums.RoomType.RECYCLING:
        return room_design.room_type_properties.recycling_room_properties
    if room_type == enums.RoomType.RESEARCH:
        return room_design.room_type_properties.research_room_properties
    if room_type == enums.RoomType.SHIELD:
        return room_design.room_type_properties.shield_room_properties
    if room_type == enums.RoomType.STATION_MISSILE:
        return room_design.room_type_properties.station_missile_properties
    if room_type == enums.RoomType.STEALTH:
        return room_design.room_type_properties.stealth_room_properties
    if room_type == enums.RoomType.STORAGE:
        return room_design.room_type_properties.storage_room_properties
    if room_type == enums.RoomType.SUPER_WEAPON:
        return room_design.room_type_properties.super_weapon_room_properties
    if room_type == enums.RoomType.SUPPLY:
        return room_design.room_type_properties.resource_room_properties
    if room_type == enums.RoomType.TELEPORT:
        return room_design.room_type_properties.teleport_room_properties
    if room_type == enums.RoomType.TRAINING:
        return room_design.room_type_properties.training_room_properties
    if room_type == enums.RoomType.TRAP:
        return room_design.room_type_properties.trap_room_properties
    if room_type == enums.RoomType.WALL:
        return room_design.room_type_properties.wall_room_properties
    return None
