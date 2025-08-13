"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class TrainingDesignRaw(EntityBaseRaw, tag="TrainingDesign"):
    XML_NODE_NAME: str = "TrainingDesign"

    ability_chance: Optional[int] = attr(name="AbilityChance", default=None)
    attack_chance: Optional[int] = attr(name="AttackChance", default=None)
    duration: Optional[int] = attr(name="Duration", default=None)
    engine_chance: Optional[int] = attr(name="EngineChance", default=None)
    fatigue: Optional[int] = attr(name="Fatigue", default=None)
    gas_cost: Optional[int] = attr(name="GasCost", default=None)
    hp_chance: Optional[int] = attr(name="HpChance", default=None)
    mineral_cost: Optional[int] = attr(name="MineralCost", default=None)
    minimum_guarantee: Optional[int] = attr(name="MinimumGuarantee", default=None)
    pilot_chance: Optional[int] = attr(name="PilotChance", default=None)
    rank: Optional[int] = attr(name="Rank", default=None)
    repair_chance: Optional[int] = attr(name="RepairChance", default=None)
    required_research_design_id: Optional[int] = attr(name="RequiredResearchDesignId", default=None)
    required_room_level: Optional[int] = attr(name="RequiredRoomLevel", default=None)
    required_training_design_id: Optional[int] = attr(name="RequiredTrainingDesignId", default=None)
    science_chance: Optional[int] = attr(name="ScienceChance", default=None)
    stamina_chance: Optional[int] = attr(name="StaminaChance", default=None)
    training_animation_style: Optional[str] = attr(name="TrainingAnimationStyle", default=None)
    training_description: Optional[str] = attr(name="TrainingDescription", default=None)
    training_design_id: Optional[int] = attr(name="TrainingDesignId", default=None)
    training_name: Optional[str] = attr(name="TrainingName", default=None)
    training_sprite_id: Optional[int] = attr(name="TrainingSpriteId", default=None)
    weapon_chance: Optional[int] = attr(name="WeaponChance", default=None)
    xp_chance: Optional[int] = attr(name="XpChance", default=None)

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


__all__ = [
    "TrainingDesignRaw",
]
