"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class TrainingDesignRaw:
    XML_NODE_NAME: str = 'TrainingDesign'

    def __init__(self, training_design_info: _EntityInfo) -> None:
        self.__required_training_design_id: int = _parse.pss_int(
            training_design_info.get('RequiredTrainingDesignId'))
        self.__gas_cost: int = _parse.pss_int(
            training_design_info.get('GasCost'))
        self.__required_research_design_id: int = _parse.pss_int(
            training_design_info.get('RequiredResearchDesignId'))
        self.__required_room_level: int = _parse.pss_int(
            training_design_info.get('RequiredRoomLevel'))
        self.__pilot_chance: int = _parse.pss_int(
            training_design_info.get('PilotChance'))
        self.__hp_chance: int = _parse.pss_int(
            training_design_info.get('HpChance'))
        self.__training_description: str = _parse.pss_str(
            training_design_info.get('TrainingDescription'))
        self.__xp_chance: int = _parse.pss_int(
            training_design_info.get('XpChance'))
        self.__science_chance: int = _parse.pss_int(
            training_design_info.get('ScienceChance'))
        self.__rank: int = _parse.pss_int(training_design_info.get('Rank'))
        self.__training_animation_style: str = _parse.pss_str(
            training_design_info.get('TrainingAnimationStyle'))
        self.__mineral_cost: int = _parse.pss_int(
            training_design_info.get('MineralCost'))
        self.__training_name: str = _parse.pss_str(
            training_design_info.get('TrainingName'))
        self.__weapon_chance: int = _parse.pss_int(
            training_design_info.get('WeaponChance'))
        self.__fatigue: int = _parse.pss_int(
            training_design_info.get('Fatigue'))
        self.__duration: int = _parse.pss_int(
            training_design_info.get('Duration'))
        self.__training_design_id: int = _parse.pss_int(
            training_design_info.get('TrainingDesignId'))
        self.__training_sprite_id: int = _parse.pss_int(
            training_design_info.get('TrainingSpriteId'))
        self.__engine_chance: int = _parse.pss_int(
            training_design_info.get('EngineChance'))
        self.__stamina_chance: int = _parse.pss_int(
            training_design_info.get('StaminaChance'))
        self.__ability_chance: int = _parse.pss_int(
            training_design_info.get('AbilityChance'))
        self.__attack_chance: int = _parse.pss_int(
            training_design_info.get('AttackChance'))
        self.__repair_chance: int = _parse.pss_int(
            training_design_info.get('RepairChance'))
        self.__minimum_guarantee: int = _parse.pss_int(
            training_design_info.get('MinimumGuarantee'))

    @property
    def required_training_design_id(self) -> int:
        return self.__required_training_design_id

    @property
    def gas_cost(self) -> int:
        return self.__gas_cost

    @property
    def required_research_design_id(self) -> int:
        return self.__required_research_design_id

    @property
    def required_room_level(self) -> int:
        return self.__required_room_level

    @property
    def pilot_chance(self) -> int:
        return self.__pilot_chance

    @property
    def hp_chance(self) -> int:
        return self.__hp_chance

    @property
    def training_description(self) -> str:
        return self.__training_description

    @property
    def xp_chance(self) -> int:
        return self.__xp_chance

    @property
    def science_chance(self) -> int:
        return self.__science_chance

    @property
    def rank(self) -> int:
        return self.__rank

    @property
    def training_animation_style(self) -> str:
        return self.__training_animation_style

    @property
    def mineral_cost(self) -> int:
        return self.__mineral_cost

    @property
    def training_name(self) -> str:
        return self.__training_name

    @property
    def weapon_chance(self) -> int:
        return self.__weapon_chance

    @property
    def fatigue(self) -> int:
        return self.__fatigue

    @property
    def duration(self) -> int:
        return self.__duration

    @property
    def training_design_id(self) -> int:
        return self.__training_design_id

    @property
    def training_sprite_id(self) -> int:
        return self.__training_sprite_id

    @property
    def engine_chance(self) -> int:
        return self.__engine_chance

    @property
    def stamina_chance(self) -> int:
        return self.__stamina_chance

    @property
    def ability_chance(self) -> int:
        return self.__ability_chance

    @property
    def attack_chance(self) -> int:
        return self.__attack_chance

    @property
    def repair_chance(self) -> int:
        return self.__repair_chance

    @property
    def minimum_guarantee(self) -> int:
        return self.__minimum_guarantee
