####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterRaw():
    XML_NODE_NAME: str = 'Character'

    def __init__(self, character_info: _EntityInfo) -> None:
        self.__training_design_id: int = _parse.pss_int(character_info.get('TrainingDesignId'))
        self.__level: int = _parse.pss_int(character_info.get('Level'))
        self.__stamina_improvement: int = _parse.pss_int(character_info.get('StaminaImprovement'))
        self.__character_name: str = _parse.pss_str(character_info.get('CharacterName'))
        self.__repair_improvement: int = _parse.pss_int(character_info.get('RepairImprovement'))
        self.__available_date: datetime = _parse.pss_datetime(character_info.get('AvailableDate'))
        self.__item_ids: str = _parse.pss_str(character_info.get('ItemIds'))
        self.__character_id: int = _parse.pss_int(character_info.get('CharacterId'))
        self.__room_id: int = _parse.pss_int(character_info.get('RoomId'))
        self.__stamina: int = _parse.pss_int(character_info.get('Stamina'))
        self.__flags: int = _parse.pss_int(character_info.get('Flags'))
        self.__owner_ship_id: int = _parse.pss_int(character_info.get('OwnerShipId'))
        self.__science_improvement: int = _parse.pss_int(character_info.get('ScienceImprovement'))
        self.__weapon_improvement: int = _parse.pss_int(character_info.get('WeaponImprovement'))
        self.__engine_improvement: int = _parse.pss_int(character_info.get('EngineImprovement'))
        self.__fatigue: int = _parse.pss_int(character_info.get('Fatigue'))
        self.__ability_improvement: int = _parse.pss_int(character_info.get('AbilityImprovement'))
        self.__training_end_date: datetime = _parse.pss_datetime(character_info.get('TrainingEndDate'))
        self.__hp_improvement: int = _parse.pss_int(character_info.get('HpImprovement'))
        self.__xp: int = _parse.pss_int(character_info.get('Xp'))
        self.__ship_id: int = _parse.pss_int(character_info.get('ShipId'))
        self.__is_new: bool = _parse.pss_bool(character_info.get('IsNew'))
        self.__training_data: str = _parse.pss_str(character_info.get('TrainingData'))
        self.__deployment_date: datetime = _parse.pss_datetime(character_info.get('DeploymentDate'))
        self.__pilot_improvement: int = _parse.pss_int(character_info.get('PilotImprovement'))
        self.__character_design_id: int = _parse.pss_int(character_info.get('CharacterDesignId'))
        self.__attack_improvement: int = _parse.pss_int(character_info.get('AttackImprovement'))

    @property
    def training_design_id(self) -> int:
        return self.__training_design_id

    @property
    def level(self) -> int:
        return self.__level

    @property
    def stamina_improvement(self) -> int:
        return self.__stamina_improvement

    @property
    def character_name(self) -> str:
        return self.__character_name

    @property
    def repair_improvement(self) -> int:
        return self.__repair_improvement

    @property
    def available_date(self) -> datetime:
        return self.__available_date

    @property
    def item_ids(self) -> str:
        return self.__item_ids

    @property
    def character_id(self) -> int:
        return self.__character_id

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def stamina(self) -> int:
        return self.__stamina

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def owner_ship_id(self) -> int:
        return self.__owner_ship_id

    @property
    def science_improvement(self) -> int:
        return self.__science_improvement

    @property
    def weapon_improvement(self) -> int:
        return self.__weapon_improvement

    @property
    def engine_improvement(self) -> int:
        return self.__engine_improvement

    @property
    def fatigue(self) -> int:
        return self.__fatigue

    @property
    def ability_improvement(self) -> int:
        return self.__ability_improvement

    @property
    def training_end_date(self) -> datetime:
        return self.__training_end_date

    @property
    def hp_improvement(self) -> int:
        return self.__hp_improvement

    @property
    def xp(self) -> int:
        return self.__xp

    @property
    def ship_id(self) -> int:
        return self.__ship_id

    @property
    def is_new(self) -> bool:
        return self.__is_new

    @property
    def training_data(self) -> str:
        return self.__training_data

    @property
    def deployment_date(self) -> datetime:
        return self.__deployment_date

    @property
    def pilot_improvement(self) -> int:
        return self.__pilot_improvement

    @property
    def character_design_id(self) -> int:
        return self.__character_design_id

    @property
    def attack_improvement(self) -> int:
        return self.__attack_improvement