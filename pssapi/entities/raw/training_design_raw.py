"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class TrainingDesignRaw:
    XML_NODE_NAME: str = 'TrainingDesign'

    def __init__(self, training_design_info: _EntityInfo) -> None:
        self.ability_chance: int = _parse.pss_int(
            training_design_info.get('AbilityChance'))
        self.attack_chance: int = _parse.pss_int(
            training_design_info.get('AttackChance'))
        self.duration: int = _parse.pss_int(
            training_design_info.get('Duration'))
        self.engine_chance: int = _parse.pss_int(
            training_design_info.get('EngineChance'))
        self.fatigue: int = _parse.pss_int(training_design_info.get('Fatigue'))
        self.gas_cost: int = _parse.pss_int(
            training_design_info.get('GasCost'))
        self.hp_chance: int = _parse.pss_int(
            training_design_info.get('HpChance'))
        self.mineral_cost: int = _parse.pss_int(
            training_design_info.get('MineralCost'))
        self.minimum_guarantee: int = _parse.pss_int(
            training_design_info.get('MinimumGuarantee'))
        self.pilot_chance: int = _parse.pss_int(
            training_design_info.get('PilotChance'))
        self.rank: int = _parse.pss_int(training_design_info.get('Rank'))
        self.repair_chance: int = _parse.pss_int(
            training_design_info.get('RepairChance'))
        self.required_research_design_id: int = _parse.pss_int(
            training_design_info.get('RequiredResearchDesignId'))
        self.required_room_level: int = _parse.pss_int(
            training_design_info.get('RequiredRoomLevel'))
        self.required_training_design_id: int = _parse.pss_int(
            training_design_info.get('RequiredTrainingDesignId'))
        self.science_chance: int = _parse.pss_int(
            training_design_info.get('ScienceChance'))
        self.stamina_chance: int = _parse.pss_int(
            training_design_info.get('StaminaChance'))
        self.training_animation_style: str = _parse.pss_str(
            training_design_info.get('TrainingAnimationStyle'))
        self.training_description: str = _parse.pss_str(
            training_design_info.get('TrainingDescription'))
        self.training_design_id: int = _parse.pss_int(
            training_design_info.get('TrainingDesignId'))
        self.training_name: str = _parse.pss_str(
            training_design_info.get('TrainingName'))
        self.training_sprite_id: int = _parse.pss_int(
            training_design_info.get('TrainingSpriteId'))
        self.weapon_chance: int = _parse.pss_int(
            training_design_info.get('WeaponChance'))
        self.xp_chance: int = _parse.pss_int(
            training_design_info.get('XpChance'))
