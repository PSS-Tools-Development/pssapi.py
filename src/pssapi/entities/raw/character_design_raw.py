"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, List, Optional

from pydantic_xml import attr, element, wrapped


if TYPE_CHECKING:
    from pssapi import entities

from .entity_base_raw import EntityBaseRaw


class CharacterDesignRaw(EntityBaseRaw, tag="CharacterDesign"):
    XML_NODE_NAME: str = "CharacterDesign"

    action_sound_file_id: Optional[int] = attr(name="ActionSoundFileId", default=None)
    attack: Optional[float] = attr(name="Attack", default=None)
    boost_values_string: Optional[str] = attr(name="BoostValuesString", default=None)
    character_body_part_id: Optional[int] = attr(name="CharacterBodyPartId", default=None)
    character_design_description: Optional[str] = attr(name="CharacterDesignDescription", default=None)
    character_design_id: Optional[int] = attr(name="CharacterDesignId", default=None)
    character_design_name: Optional[str] = attr(name="CharacterDesignName", default=None)
    character_head_part_id: Optional[int] = attr(name="CharacterHeadPartId", default=None)
    character_leg_part_id: Optional[int] = attr(name="CharacterLegPartId", default=None)
    character_parts: List["entities.CharacterPart"] = wrapped("CharacterParts", element(tag="CharacterPart", default_factory=list))
    collection_design_id: Optional[int] = attr(name="CollectionDesignId", default=None)
    engine: Optional[float] = attr(name="Engine", default=None)
    equipment_mask: Optional[int] = attr(name="EquipmentMask", default=None)
    final_attack: Optional[float] = attr(name="FinalAttack", default=None)
    final_engine: Optional[float] = attr(name="FinalEngine", default=None)
    final_hp: Optional[int] = attr(name="FinalHp", default=None)
    final_pilot: Optional[float] = attr(name="FinalPilot", default=None)
    final_repair: Optional[float] = attr(name="FinalRepair", default=None)
    final_research: Optional[int] = attr(name="FinalResearch", default=None)
    final_science: Optional[float] = attr(name="FinalScience", default=None)
    final_weapon: Optional[float] = attr(name="FinalWeapon", default=None)
    fire_resistance: Optional[int] = attr(name="FireResistance", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    gender_type: Optional[str] = attr(name="GenderType", default=None)
    hp: Optional[int] = attr(name="Hp", default=None)
    level: Optional[int] = attr(name="Level", default=None)
    max_character_level: Optional[int] = attr(name="MaxCharacterLevel", default=None)
    max_count: Optional[int] = attr(name="MaxCount", default=None)
    min_ship_level: Optional[int] = attr(name="MinShipLevel", default=None)
    pilot: Optional[float] = attr(name="Pilot", default=None)
    profile_sprite_id: Optional[int] = attr(name="ProfileSpriteId", default=None)
    progression_type: Optional[str] = attr(name="ProgressionType", default=None)
    race_type: Optional[str] = attr(name="RaceType", default=None)
    rarity: Optional[str] = attr(name="Rarity", default=None)
    repair: Optional[float] = attr(name="Repair", default=None)
    research: Optional[int] = attr(name="Research", default=None)
    root_character_design_id: Optional[int] = attr(name="RootCharacterDesignId", default=None)
    run_speed: Optional[int] = attr(name="RunSpeed", default=None)
    science: Optional[float] = attr(name="Science", default=None)
    special_ability_argument: Optional[int] = attr(name="SpecialAbilityArgument", default=None)
    special_ability_final_argument: Optional[int] = attr(name="SpecialAbilityFinalArgument", default=None)
    special_ability_type: Optional[str] = attr(name="SpecialAbilityType", default=None)
    speech_phrases: Optional[str] = attr(name="SpeechPhrases", default=None)
    speech_pitch: Optional[int] = attr(name="SpeechPitch", default=None)
    speech_rate: Optional[int] = attr(name="SpeechRate", default=None)
    speech_voice: Optional[str] = attr(name="SpeechVoice", default=None)
    tags: Optional[str] = attr(name="Tags", default=None)
    tap_sound_file_id: Optional[int] = attr(name="TapSoundFileId", default=None)
    training_capacity: Optional[int] = attr(name="TrainingCapacity", default=None)
    walking_speed: Optional[int] = attr(name="WalkingSpeed", default=None)
    weapon: Optional[float] = attr(name="Weapon", default=None)
    xp_requirement_scale: Optional[int] = attr(name="XpRequirementScale", default=None)

    def _key(self):
        return (
            self.action_sound_file_id,
            self.attack,
            self.boost_values_string,
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
            self.tags,
            self.tap_sound_file_id,
            self.training_capacity,
            self.walking_speed,
            self.weapon,
            self.xp_requirement_scale,
        )


__all__ = [
    "CharacterDesignRaw",
]
