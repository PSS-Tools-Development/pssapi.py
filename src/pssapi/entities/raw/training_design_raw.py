"""
This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class TrainingDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "TrainingDesign"

    def __init__(self, training_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._ability_chance: int = _parse.pss_int(training_design_info.pop("AbilityChance", None))
        self._attack_chance: int = _parse.pss_int(training_design_info.pop("AttackChance", None))
        self._duration: int = _parse.pss_int(training_design_info.pop("Duration", None))
        self._engine_chance: int = _parse.pss_int(training_design_info.pop("EngineChance", None))
        self._fatigue: int = _parse.pss_int(training_design_info.pop("Fatigue", None))
        self._gas_cost: int = _parse.pss_int(training_design_info.pop("GasCost", None))
        self._hp_chance: int = _parse.pss_int(training_design_info.pop("HpChance", None))
        self._mineral_cost: int = _parse.pss_int(training_design_info.pop("MineralCost", None))
        self._minimum_guarantee: int = _parse.pss_int(training_design_info.pop("MinimumGuarantee", None))
        self._pilot_chance: int = _parse.pss_int(training_design_info.pop("PilotChance", None))
        self._rank: int = _parse.pss_int(training_design_info.pop("Rank", None))
        self._repair_chance: int = _parse.pss_int(training_design_info.pop("RepairChance", None))
        self._required_research_design_id: int = _parse.pss_int(training_design_info.pop("RequiredResearchDesignId", None))
        self._required_room_level: int = _parse.pss_int(training_design_info.pop("RequiredRoomLevel", None))
        self._required_training_design_id: int = _parse.pss_int(training_design_info.pop("RequiredTrainingDesignId", None))
        self._science_chance: int = _parse.pss_int(training_design_info.pop("ScienceChance", None))
        self._stamina_chance: int = _parse.pss_int(training_design_info.pop("StaminaChance", None))
        self._training_animation_style: str = _parse.pss_str(training_design_info.pop("TrainingAnimationStyle", None))
        self._training_description: str = _parse.pss_str(training_design_info.pop("TrainingDescription", None))
        self._training_design_id: int = _parse.pss_int(training_design_info.pop("TrainingDesignId", None))
        self._training_name: str = _parse.pss_str(training_design_info.pop("TrainingName", None))
        self._training_sprite_id: int = _parse.pss_int(training_design_info.pop("TrainingSpriteId", None))
        self._weapon_chance: int = _parse.pss_int(training_design_info.pop("WeaponChance", None))
        self._xp_chance: int = _parse.pss_int(training_design_info.pop("XpChance", None))
        super().__init__(training_design_info)

    @property
    def ability_chance(self) -> int:
        return self._ability_chance

    @property
    def attack_chance(self) -> int:
        return self._attack_chance

    @property
    def duration(self) -> int:
        return self._duration

    @property
    def engine_chance(self) -> int:
        return self._engine_chance

    @property
    def fatigue(self) -> int:
        return self._fatigue

    @property
    def gas_cost(self) -> int:
        return self._gas_cost

    @property
    def hp_chance(self) -> int:
        return self._hp_chance

    @property
    def mineral_cost(self) -> int:
        return self._mineral_cost

    @property
    def minimum_guarantee(self) -> int:
        return self._minimum_guarantee

    @property
    def pilot_chance(self) -> int:
        return self._pilot_chance

    @property
    def rank(self) -> int:
        return self._rank

    @property
    def repair_chance(self) -> int:
        return self._repair_chance

    @property
    def required_research_design_id(self) -> int:
        return self._required_research_design_id

    @property
    def required_room_level(self) -> int:
        return self._required_room_level

    @property
    def required_training_design_id(self) -> int:
        return self._required_training_design_id

    @property
    def science_chance(self) -> int:
        return self._science_chance

    @property
    def stamina_chance(self) -> int:
        return self._stamina_chance

    @property
    def training_animation_style(self) -> str:
        return self._training_animation_style

    @property
    def training_description(self) -> str:
        return self._training_description

    @property
    def training_design_id(self) -> int:
        return self._training_design_id

    @property
    def training_name(self) -> str:
        return self._training_name

    @property
    def training_sprite_id(self) -> int:
        return self._training_sprite_id

    @property
    def weapon_chance(self) -> int:
        return self._weapon_chance

    @property
    def xp_chance(self) -> int:
        return self._xp_chance

    def _key(self):
        return (
            self.ability_chance,
            self.attack_chance,
            self.duration,
            self.engine_chance,
            self.fatigue,
            self.gas_cost,
            self.hp_chance,
            self.mineral_cost,
            self.minimum_guarantee,
            self.pilot_chance,
            self.rank,
            self.repair_chance,
            self.required_research_design_id,
            self.required_room_level,
            self.required_training_design_id,
            self.science_chance,
            self.stamina_chance,
            self.training_animation_style,
            self.training_description,
            self.training_design_id,
            self.training_name,
            self.training_sprite_id,
            self.weapon_chance,
            self.xp_chance,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AbilityChance": self.ability_chance,
                "AttackChance": self.attack_chance,
                "Duration": self.duration,
                "EngineChance": self.engine_chance,
                "Fatigue": self.fatigue,
                "GasCost": self.gas_cost,
                "HpChance": self.hp_chance,
                "MineralCost": self.mineral_cost,
                "MinimumGuarantee": self.minimum_guarantee,
                "PilotChance": self.pilot_chance,
                "Rank": self.rank,
                "RepairChance": self.repair_chance,
                "RequiredResearchDesignId": self.required_research_design_id,
                "RequiredRoomLevel": self.required_room_level,
                "RequiredTrainingDesignId": self.required_training_design_id,
                "ScienceChance": self.science_chance,
                "StaminaChance": self.stamina_chance,
                "TrainingAnimationStyle": self.training_animation_style,
                "TrainingDescription": self.training_description,
                "TrainingDesignId": self.training_design_id,
                "TrainingName": self.training_name,
                "TrainingSpriteId": self.training_sprite_id,
                "WeaponChance": self.weapon_chance,
                "XpChance": self.xp_chance,
            }
            self._dict.update(super().__dict__())

        return self._dict
