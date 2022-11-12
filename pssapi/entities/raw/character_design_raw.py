"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterDesignRaw:
    XML_NODE_NAME: str = 'CharacterDesign'

    def __init__(self, character_design_info: _EntityInfo) -> None:
        self.action_sound_file_id: int = _parse.pss_int(
            character_design_info.get('ActionSoundFileId'))
        self.attack: float = _parse.pss_float(
            character_design_info.get('Attack'))
        self.character_body_part_id: int = _parse.pss_int(
            character_design_info.get('CharacterBodyPartId'))
        self.character_design_description: str = _parse.pss_str(
            character_design_info.get('CharacterDesignDescription'))
        self.character_design_id: int = _parse.pss_int(
            character_design_info.get('CharacterDesignId'))
        self.character_design_name: str = _parse.pss_str(
            character_design_info.get('CharacterDesignName'))
        self.character_head_part_id: int = _parse.pss_int(
            character_design_info.get('CharacterHeadPartId'))
        self.character_leg_part_id: int = _parse.pss_int(
            character_design_info.get('CharacterLegPartId'))
        self.collection_design_id: int = _parse.pss_int(
            character_design_info.get('CollectionDesignId'))
        self.engine: float = _parse.pss_float(
            character_design_info.get('Engine'))
        self.equipment_mask: int = _parse.pss_int(
            character_design_info.get('EquipmentMask'))
        self.final_attack: float = _parse.pss_float(
            character_design_info.get('FinalAttack'))
        self.final_engine: float = _parse.pss_float(
            character_design_info.get('FinalEngine'))
        self.final_hp: int = _parse.pss_int(
            character_design_info.get('FinalHp'))
        self.final_pilot: int = _parse.pss_int(
            character_design_info.get('FinalPilot'))
        self.final_repair: float = _parse.pss_float(
            character_design_info.get('FinalRepair'))
        self.final_research: int = _parse.pss_int(
            character_design_info.get('FinalResearch'))
        self.final_science: float = _parse.pss_float(
            character_design_info.get('FinalScience'))
        self.final_weapon: float = _parse.pss_float(
            character_design_info.get('FinalWeapon'))
        self.fire_resistance: int = _parse.pss_int(
            character_design_info.get('FireResistance'))
        self.flags: int = _parse.pss_int(character_design_info.get('Flags'))
        self.gender_type: str = _parse.pss_str(
            character_design_info.get('GenderType'))
        self.hp: int = _parse.pss_int(character_design_info.get('Hp'))
        self.level: int = _parse.pss_int(character_design_info.get('Level'))
        self.max_character_level: int = _parse.pss_int(
            character_design_info.get('MaxCharacterLevel'))
        self.max_count: int = _parse.pss_int(
            character_design_info.get('MaxCount'))
        self.min_ship_level: int = _parse.pss_int(
            character_design_info.get('MinShipLevel'))
        self.pilot: float = _parse.pss_float(
            character_design_info.get('Pilot'))
        self.profile_sprite_id: int = _parse.pss_int(
            character_design_info.get('ProfileSpriteId'))
        self.progression_type: str = _parse.pss_str(
            character_design_info.get('ProgressionType'))
        self.race_type: str = _parse.pss_str(
            character_design_info.get('RaceType'))
        self.rarity: str = _parse.pss_str(character_design_info.get('Rarity'))
        self.repair: float = _parse.pss_float(
            character_design_info.get('Repair'))
        self.research: int = _parse.pss_int(
            character_design_info.get('Research'))
        self.root_character_design_id: int = _parse.pss_int(
            character_design_info.get('RootCharacterDesignId'))
        self.run_speed: int = _parse.pss_int(
            character_design_info.get('RunSpeed'))
        self.science: float = _parse.pss_float(
            character_design_info.get('Science'))
        self.special_ability_argument: int = _parse.pss_int(
            character_design_info.get('SpecialAbilityArgument'))
        self.special_ability_final_argument: int = _parse.pss_int(
            character_design_info.get('SpecialAbilityFinalArgument'))
        self.special_ability_type: str = _parse.pss_str(
            character_design_info.get('SpecialAbilityType'))
        self.speech_phrases: str = _parse.pss_str(
            character_design_info.get('SpeechPhrases'))
        self.speech_pitch: int = _parse.pss_int(
            character_design_info.get('SpeechPitch'))
        self.speech_rate: int = _parse.pss_int(
            character_design_info.get('SpeechRate'))
        self.speech_voice: str = _parse.pss_str(
            character_design_info.get('SpeechVoice'))
        self.tap_sound_file_id: int = _parse.pss_int(
            character_design_info.get('TapSoundFileId'))
        self.training_capacity: int = _parse.pss_int(
            character_design_info.get('TrainingCapacity'))
        self.walking_speed: int = _parse.pss_int(
            character_design_info.get('WalkingSpeed'))
        self.weapon: float = _parse.pss_float(
            character_design_info.get('Weapon'))
        self.xp_requirement_scale: int = _parse.pss_int(
            character_design_info.get('XpRequirementScale'))
