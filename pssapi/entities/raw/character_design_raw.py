"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterDesignRaw:
    XML_NODE_NAME: str = 'CharacterDesign'

    def __init__(self, character_design_info: _EntityInfo) -> None:
        self.__character_design_id: int = _parse.pss_int(
            character_design_info.get('CharacterDesignId'))
        self.__character_design_name: str = _parse.pss_str(
            character_design_info.get('CharacterDesignName'))
        self.__character_head_part_id: int = _parse.pss_int(
            character_design_info.get('CharacterHeadPartId'))
        self.__character_body_part_id: int = _parse.pss_int(
            character_design_info.get('CharacterBodyPartId'))
        self.__gender_type: str = _parse.pss_str(
            character_design_info.get('GenderType'))
        self.__race_type: str = _parse.pss_str(
            character_design_info.get('RaceType'))
        self.__hp: int = _parse.pss_int(character_design_info.get('Hp'))
        self.__pilot: int = _parse.pss_int(character_design_info.get('Pilot'))
        self.__attack: int = _parse.pss_int(
            character_design_info.get('Attack'))
        self.__fire_resistance: int = _parse.pss_int(
            character_design_info.get('FireResistance'))
        self.__repair: int = _parse.pss_int(
            character_design_info.get('Repair'))
        self.__weapon: int = _parse.pss_int(
            character_design_info.get('Weapon'))
        self.__science: int = _parse.pss_int(
            character_design_info.get('Science'))
        self.__engine: int = _parse.pss_int(
            character_design_info.get('Engine'))
        self.__research: int = _parse.pss_int(
            character_design_info.get('Research'))
        self.__level: int = _parse.pss_int(character_design_info.get('Level'))
        self.__walking_speed: int = _parse.pss_int(
            character_design_info.get('WalkingSpeed'))
        self.__min_ship_level: int = _parse.pss_int(
            character_design_info.get('MinShipLevel'))
        self.__final_hp: int = _parse.pss_int(
            character_design_info.get('FinalHp'))
        self.__final_pilot: int = _parse.pss_int(
            character_design_info.get('FinalPilot'))
        self.__final_attack: float = _parse.pss_float(
            character_design_info.get('FinalAttack'))
        self.__final_repair: float = _parse.pss_float(
            character_design_info.get('FinalRepair'))
        self.__final_weapon: int = _parse.pss_int(
            character_design_info.get('FinalWeapon'))
        self.__final_science: int = _parse.pss_int(
            character_design_info.get('FinalScience'))
        self.__final_engine: int = _parse.pss_int(
            character_design_info.get('FinalEngine'))
        self.__final_research: int = _parse.pss_int(
            character_design_info.get('FinalResearch'))
        self.__character_leg_part_id: int = _parse.pss_int(
            character_design_info.get('CharacterLegPartId'))
        self.__rarity: str = _parse.pss_str(
            character_design_info.get('Rarity'))
        self.__progression_type: str = _parse.pss_str(
            character_design_info.get('ProgressionType'))
        self.__character_design_description: str = _parse.pss_str(
            character_design_info.get('CharacterDesignDescription'))
        self.__xp_requirement_scale: int = _parse.pss_int(
            character_design_info.get('XpRequirementScale'))
        self.__max_character_level: int = _parse.pss_int(
            character_design_info.get('MaxCharacterLevel'))
        self.__special_ability_type: str = _parse.pss_str(
            character_design_info.get('SpecialAbilityType'))
        self.__special_ability_argument: int = _parse.pss_int(
            character_design_info.get('SpecialAbilityArgument'))
        self.__special_ability_final_argument: int = _parse.pss_int(
            character_design_info.get('SpecialAbilityFinalArgument'))
        self.__profile_sprite_id: int = _parse.pss_int(
            character_design_info.get('ProfileSpriteId'))
        self.__run_speed: int = _parse.pss_int(
            character_design_info.get('RunSpeed'))
        self.__training_capacity: int = _parse.pss_int(
            character_design_info.get('TrainingCapacity'))
        self.__equipment_mask: int = _parse.pss_int(
            character_design_info.get('EquipmentMask'))
        self.__speech_voice: str = _parse.pss_str(
            character_design_info.get('SpeechVoice'))
        self.__speech_phrases: str = _parse.pss_str(
            character_design_info.get('SpeechPhrases'))
        self.__speech_rate: int = _parse.pss_int(
            character_design_info.get('SpeechRate'))
        self.__speech_pitch: int = _parse.pss_int(
            character_design_info.get('SpeechPitch'))
        self.__flags: int = _parse.pss_int(character_design_info.get('Flags'))
        self.__root_character_design_id: int = _parse.pss_int(
            character_design_info.get('RootCharacterDesignId'))
        self.__max_count: int = _parse.pss_int(
            character_design_info.get('MaxCount'))
        self.__tap_sound_file_id: int = _parse.pss_int(
            character_design_info.get('TapSoundFileId'))
        self.__action_sound_file_id: int = _parse.pss_int(
            character_design_info.get('ActionSoundFileId'))
        self.__collection_design_id: int = _parse.pss_int(
            character_design_info.get('CollectionDesignId'))

    @property
    def character_design_id(self) -> int:
        return self.__character_design_id

    @property
    def character_design_name(self) -> str:
        return self.__character_design_name

    @property
    def character_head_part_id(self) -> int:
        return self.__character_head_part_id

    @property
    def character_body_part_id(self) -> int:
        return self.__character_body_part_id

    @property
    def gender_type(self) -> str:
        return self.__gender_type

    @property
    def race_type(self) -> str:
        return self.__race_type

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def pilot(self) -> int:
        return self.__pilot

    @property
    def attack(self) -> int:
        return self.__attack

    @property
    def fire_resistance(self) -> int:
        return self.__fire_resistance

    @property
    def repair(self) -> int:
        return self.__repair

    @property
    def weapon(self) -> int:
        return self.__weapon

    @property
    def science(self) -> int:
        return self.__science

    @property
    def engine(self) -> int:
        return self.__engine

    @property
    def research(self) -> int:
        return self.__research

    @property
    def level(self) -> int:
        return self.__level

    @property
    def walking_speed(self) -> int:
        return self.__walking_speed

    @property
    def min_ship_level(self) -> int:
        return self.__min_ship_level

    @property
    def final_hp(self) -> int:
        return self.__final_hp

    @property
    def final_pilot(self) -> int:
        return self.__final_pilot

    @property
    def final_attack(self) -> float:
        return self.__final_attack

    @property
    def final_repair(self) -> float:
        return self.__final_repair

    @property
    def final_weapon(self) -> int:
        return self.__final_weapon

    @property
    def final_science(self) -> int:
        return self.__final_science

    @property
    def final_engine(self) -> int:
        return self.__final_engine

    @property
    def final_research(self) -> int:
        return self.__final_research

    @property
    def character_leg_part_id(self) -> int:
        return self.__character_leg_part_id

    @property
    def rarity(self) -> str:
        return self.__rarity

    @property
    def progression_type(self) -> str:
        return self.__progression_type

    @property
    def character_design_description(self) -> str:
        return self.__character_design_description

    @property
    def xp_requirement_scale(self) -> int:
        return self.__xp_requirement_scale

    @property
    def max_character_level(self) -> int:
        return self.__max_character_level

    @property
    def special_ability_type(self) -> str:
        return self.__special_ability_type

    @property
    def special_ability_argument(self) -> int:
        return self.__special_ability_argument

    @property
    def special_ability_final_argument(self) -> int:
        return self.__special_ability_final_argument

    @property
    def profile_sprite_id(self) -> int:
        return self.__profile_sprite_id

    @property
    def run_speed(self) -> int:
        return self.__run_speed

    @property
    def training_capacity(self) -> int:
        return self.__training_capacity

    @property
    def equipment_mask(self) -> int:
        return self.__equipment_mask

    @property
    def speech_voice(self) -> str:
        return self.__speech_voice

    @property
    def speech_phrases(self) -> str:
        return self.__speech_phrases

    @property
    def speech_rate(self) -> int:
        return self.__speech_rate

    @property
    def speech_pitch(self) -> int:
        return self.__speech_pitch

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def root_character_design_id(self) -> int:
        return self.__root_character_design_id

    @property
    def max_count(self) -> int:
        return self.__max_count

    @property
    def tap_sound_file_id(self) -> int:
        return self.__tap_sound_file_id

    @property
    def action_sound_file_id(self) -> int:
        return self.__action_sound_file_id

    @property
    def collection_design_id(self) -> int:
        return self.__collection_design_id
