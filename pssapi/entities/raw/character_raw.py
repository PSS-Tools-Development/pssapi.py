"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterRaw:
    XML_NODE_NAME: str = 'Character'

    def __init__(self, character_info: _EntityInfo) -> None:
        self.ability_improvement: int = _parse.pss_int(character_info.get('AbilityImprovement'))
        self.attack_improvement: int = _parse.pss_int(character_info.get('AttackImprovement'))
        self.available_date: _datetime = _parse.pss__datetime(character_info.get('AvailableDate'))
        self.character_design_id: int = _parse.pss_int(character_info.get('CharacterDesignId'))
        self.character_id: int = _parse.pss_int(character_info.get('CharacterId'))
        self.character_name: str = _parse.pss_str(character_info.get('CharacterName'))
        self.deployment_date: str = _parse.pss_str(character_info.get('DeploymentDate'))
        self.engine_improvement: int = _parse.pss_int(character_info.get('EngineImprovement'))
        self.fatigue: int = _parse.pss_int(character_info.get('Fatigue'))
        self.flags: int = _parse.pss_int(character_info.get('Flags'))
        self.hp_improvement: int = _parse.pss_int(character_info.get('HpImprovement'))
        self.is_new: bool = _parse.pss_bool(character_info.get('IsNew'))
        self.item_ids: str = _parse.pss_str(character_info.get('ItemIds'))
        self.level: int = _parse.pss_int(character_info.get('Level'))
        self.owner_ship_id: int = _parse.pss_int(character_info.get('OwnerShipId'))
        self.pilot_improvement: int = _parse.pss_int(character_info.get('PilotImprovement'))
        self.repair_improvement: int = _parse.pss_int(character_info.get('RepairImprovement'))
        self.room_id: int = _parse.pss_int(character_info.get('RoomId'))
        self.science_improvement: int = _parse.pss_int(character_info.get('ScienceImprovement'))
        self.ship_id: int = _parse.pss_int(character_info.get('ShipId'))
        self.stamina: int = _parse.pss_int(character_info.get('Stamina'))
        self.stamina_improvement: int = _parse.pss_int(character_info.get('StaminaImprovement'))
        self.training_data: str = _parse.pss_str(character_info.get('TrainingData'))
        self.training_design_id: int = _parse.pss_int(character_info.get('TrainingDesignId'))
        self.training_end_date: str = _parse.pss_str(character_info.get('TrainingEndDate'))
        self.weapon_improvement: int = _parse.pss_int(character_info.get('WeaponImprovement'))
        self.xp: int = _parse.pss_int(character_info.get('Xp'))
