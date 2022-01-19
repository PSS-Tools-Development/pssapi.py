"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict
from typing import List as _List

import pssapi.entities as _entities

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterDesignRaw:
    XML_NODE_NAME: str = "CharacterDesign"

    def __init__(self, character_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._action_sound_file_id: int = _parse.pss_int(character_design_info.get("ActionSoundFileId"))
        self._attack: float = _parse.pss_float(character_design_info.get("Attack"))
        self._character_body_part_id: int = _parse.pss_int(character_design_info.get("CharacterBodyPartId"))
        self._character_design_description: str = _parse.pss_str(character_design_info.get("CharacterDesignDescription"))
        self._character_design_id: int = _parse.pss_int(character_design_info.get("CharacterDesignId"))
        self._character_design_name: str = _parse.pss_str(character_design_info.get("CharacterDesignName"))
        self._character_head_part_id: int = _parse.pss_int(character_design_info.get("CharacterHeadPartId"))
        self._character_leg_part_id: int = _parse.pss_int(character_design_info.get("CharacterLegPartId"))
        self._character_parts: _List[_entities.CharacterPart] = (
            [_entities.CharacterPart(child_info) for child_info in character_design_info.get("CharacterParts")] if character_design_info.get("CharacterParts") else []
        )
        self._collection_design_id: int = _parse.pss_int(character_design_info.get("CollectionDesignId"))
        self._engine: float = _parse.pss_float(character_design_info.get("Engine"))
        self._equipment_mask: int = _parse.pss_int(character_design_info.get("EquipmentMask"))
        self._final_attack: float = _parse.pss_float(character_design_info.get("FinalAttack"))
        self._final_engine: float = _parse.pss_float(character_design_info.get("FinalEngine"))
        self._final_hp: int = _parse.pss_int(character_design_info.get("FinalHp"))
        self._final_pilot: int = _parse.pss_int(character_design_info.get("FinalPilot"))
        self._final_repair: float = _parse.pss_float(character_design_info.get("FinalRepair"))
        self._final_research: int = _parse.pss_int(character_design_info.get("FinalResearch"))
        self._final_science: float = _parse.pss_float(character_design_info.get("FinalScience"))
        self._final_weapon: float = _parse.pss_float(character_design_info.get("FinalWeapon"))
        self._fire_resistance: int = _parse.pss_int(character_design_info.get("FireResistance"))
        self._flags: int = _parse.pss_int(character_design_info.get("Flags"))
        self._gender_type: str = _parse.pss_str(character_design_info.get("GenderType"))
        self._hp: int = _parse.pss_int(character_design_info.get("Hp"))
        self._level: int = _parse.pss_int(character_design_info.get("Level"))
        self._max_character_level: int = _parse.pss_int(character_design_info.get("MaxCharacterLevel"))
        self._max_count: int = _parse.pss_int(character_design_info.get("MaxCount"))
        self._min_ship_level: int = _parse.pss_int(character_design_info.get("MinShipLevel"))
        self._pilot: float = _parse.pss_float(character_design_info.get("Pilot"))
        self._profile_sprite_id: int = _parse.pss_int(character_design_info.get("ProfileSpriteId"))
        self._progression_type: str = _parse.pss_str(character_design_info.get("ProgressionType"))
        self._race_type: str = _parse.pss_str(character_design_info.get("RaceType"))
        self._rarity: str = _parse.pss_str(character_design_info.get("Rarity"))
        self._repair: float = _parse.pss_float(character_design_info.get("Repair"))
        self._research: int = _parse.pss_int(character_design_info.get("Research"))
        self._root_character_design_id: int = _parse.pss_int(character_design_info.get("RootCharacterDesignId"))
        self._run_speed: int = _parse.pss_int(character_design_info.get("RunSpeed"))
        self._science: float = _parse.pss_float(character_design_info.get("Science"))
        self._special_ability_argument: int = _parse.pss_int(character_design_info.get("SpecialAbilityArgument"))
        self._special_ability_final_argument: int = _parse.pss_int(character_design_info.get("SpecialAbilityFinalArgument"))
        self._special_ability_type: str = _parse.pss_str(character_design_info.get("SpecialAbilityType"))
        self._speech_phrases: str = _parse.pss_str(character_design_info.get("SpeechPhrases"))
        self._speech_pitch: int = _parse.pss_int(character_design_info.get("SpeechPitch"))
        self._speech_rate: int = _parse.pss_int(character_design_info.get("SpeechRate"))
        self._speech_voice: str = _parse.pss_str(character_design_info.get("SpeechVoice"))
        self._tap_sound_file_id: int = _parse.pss_int(character_design_info.get("TapSoundFileId"))
        self._training_capacity: int = _parse.pss_int(character_design_info.get("TrainingCapacity"))
        self._walking_speed: int = _parse.pss_int(character_design_info.get("WalkingSpeed"))
        self._weapon: float = _parse.pss_float(character_design_info.get("Weapon"))
        self._xp_requirement_scale: int = _parse.pss_int(character_design_info.get("XpRequirementScale"))

    @property
    def action_sound_file_id(self) -> int:
        return self._action_sound_file_id

    @property
    def attack(self) -> float:
        return self._attack

    @property
    def character_body_part_id(self) -> int:
        return self._character_body_part_id

    @property
    def character_design_description(self) -> str:
        return self._character_design_description

    @property
    def character_design_id(self) -> int:
        return self._character_design_id

    @property
    def character_design_name(self) -> str:
        return self._character_design_name

    @property
    def character_head_part_id(self) -> int:
        return self._character_head_part_id

    @property
    def character_leg_part_id(self) -> int:
        return self._character_leg_part_id

    @property
    def character_parts(self) -> _List["_entities.CharacterPart"]:
        return self._character_parts

    @property
    def collection_design_id(self) -> int:
        return self._collection_design_id

    @property
    def engine(self) -> float:
        return self._engine

    @property
    def equipment_mask(self) -> int:
        return self._equipment_mask

    @property
    def final_attack(self) -> float:
        return self._final_attack

    @property
    def final_engine(self) -> float:
        return self._final_engine

    @property
    def final_hp(self) -> int:
        return self._final_hp

    @property
    def final_pilot(self) -> int:
        return self._final_pilot

    @property
    def final_repair(self) -> float:
        return self._final_repair

    @property
    def final_research(self) -> int:
        return self._final_research

    @property
    def final_science(self) -> float:
        return self._final_science

    @property
    def final_weapon(self) -> float:
        return self._final_weapon

    @property
    def fire_resistance(self) -> int:
        return self._fire_resistance

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def gender_type(self) -> str:
        return self._gender_type

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def level(self) -> int:
        return self._level

    @property
    def max_character_level(self) -> int:
        return self._max_character_level

    @property
    def max_count(self) -> int:
        return self._max_count

    @property
    def min_ship_level(self) -> int:
        return self._min_ship_level

    @property
    def pilot(self) -> float:
        return self._pilot

    @property
    def profile_sprite_id(self) -> int:
        return self._profile_sprite_id

    @property
    def progression_type(self) -> str:
        return self._progression_type

    @property
    def race_type(self) -> str:
        return self._race_type

    @property
    def rarity(self) -> str:
        return self._rarity

    @property
    def repair(self) -> float:
        return self._repair

    @property
    def research(self) -> int:
        return self._research

    @property
    def root_character_design_id(self) -> int:
        return self._root_character_design_id

    @property
    def run_speed(self) -> int:
        return self._run_speed

    @property
    def science(self) -> float:
        return self._science

    @property
    def special_ability_argument(self) -> int:
        return self._special_ability_argument

    @property
    def special_ability_final_argument(self) -> int:
        return self._special_ability_final_argument

    @property
    def special_ability_type(self) -> str:
        return self._special_ability_type

    @property
    def speech_phrases(self) -> str:
        return self._speech_phrases

    @property
    def speech_pitch(self) -> int:
        return self._speech_pitch

    @property
    def speech_rate(self) -> int:
        return self._speech_rate

    @property
    def speech_voice(self) -> str:
        return self._speech_voice

    @property
    def tap_sound_file_id(self) -> int:
        return self._tap_sound_file_id

    @property
    def training_capacity(self) -> int:
        return self._training_capacity

    @property
    def walking_speed(self) -> int:
        return self._walking_speed

    @property
    def weapon(self) -> float:
        return self._weapon

    @property
    def xp_requirement_scale(self) -> int:
        return self._xp_requirement_scale

    def _key(self):
        return (
            self.action_sound_file_id,
            self.attack,
            self.character_body_part_id,
            self.character_design_description,
            self.character_design_id,
            self.character_design_name,
            self.character_head_part_id,
            self.character_leg_part_id,
            tuple(child._key() for child in self.character_parts),
            self.collection_design_id,
            self.engine,
            self.equipment_mask,
            self.final_attack,
            self.final_engine,
            self.final_hp,
            self.final_pilot,
            self.final_repair,
            self.final_research,
            self.final_science,
            self.final_weapon,
            self.fire_resistance,
            self.flags,
            self.gender_type,
            self.hp,
            self.level,
            self.max_character_level,
            self.max_count,
            self.min_ship_level,
            self.pilot,
            self.profile_sprite_id,
            self.progression_type,
            self.race_type,
            self.rarity,
            self.repair,
            self.research,
            self.root_character_design_id,
            self.run_speed,
            self.science,
            self.special_ability_argument,
            self.special_ability_final_argument,
            self.special_ability_type,
            self.speech_phrases,
            self.speech_pitch,
            self.speech_rate,
            self.speech_voice,
            self.tap_sound_file_id,
            self.training_capacity,
            self.walking_speed,
            self.weapon,
            self.xp_requirement_scale,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ActionSoundFileId": self.action_sound_file_id,
                "Attack": self.attack,
                "CharacterBodyPartId": self.character_body_part_id,
                "CharacterDesignDescription": self.character_design_description,
                "CharacterDesignId": self.character_design_id,
                "CharacterDesignName": self.character_design_name,
                "CharacterHeadPartId": self.character_head_part_id,
                "CharacterLegPartId": self.character_leg_part_id,
                "CharacterParts": [dict(child) for child in self.character_parts],
                "CollectionDesignId": self.collection_design_id,
                "Engine": self.engine,
                "EquipmentMask": self.equipment_mask,
                "FinalAttack": self.final_attack,
                "FinalEngine": self.final_engine,
                "FinalHp": self.final_hp,
                "FinalPilot": self.final_pilot,
                "FinalRepair": self.final_repair,
                "FinalResearch": self.final_research,
                "FinalScience": self.final_science,
                "FinalWeapon": self.final_weapon,
                "FireResistance": self.fire_resistance,
                "Flags": self.flags,
                "GenderType": self.gender_type,
                "Hp": self.hp,
                "Level": self.level,
                "MaxCharacterLevel": self.max_character_level,
                "MaxCount": self.max_count,
                "MinShipLevel": self.min_ship_level,
                "Pilot": self.pilot,
                "ProfileSpriteId": self.profile_sprite_id,
                "ProgressionType": self.progression_type,
                "RaceType": self.race_type,
                "Rarity": self.rarity,
                "Repair": self.repair,
                "Research": self.research,
                "RootCharacterDesignId": self.root_character_design_id,
                "RunSpeed": self.run_speed,
                "Science": self.science,
                "SpecialAbilityArgument": self.special_ability_argument,
                "SpecialAbilityFinalArgument": self.special_ability_final_argument,
                "SpecialAbilityType": self.special_ability_type,
                "SpeechPhrases": self.speech_phrases,
                "SpeechPitch": self.speech_pitch,
                "SpeechRate": self.speech_rate,
                "SpeechVoice": self.speech_voice,
                "TapSoundFileId": self.tap_sound_file_id,
                "TrainingCapacity": self.training_capacity,
                "WalkingSpeed": self.walking_speed,
                "Weapon": self.weapon,
                "XpRequirementScale": self.xp_requirement_scale,
            }

        return self._dict
