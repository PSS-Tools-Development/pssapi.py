"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from pydantic_xml import attr, element, wrapped


if TYPE_CHECKING:
    from pssapi import entities

from .entity_base_raw import EntityBaseRaw


class CharacterRaw(EntityBaseRaw, tag="Character"):
    XML_NODE_NAME: str = "Character"

    ability_improvement: Optional[int] = attr(name="AbilityImprovement", default=None)
    attack_improvement: Optional[int] = attr(name="AttackImprovement", default=None)
    available_date: Optional[datetime] = attr(name="AvailableDate", default=None)
    battle_character_hp: Optional[int] = attr(name="BattleCharacterHp", default=None)
    bloodlust_frame: Optional[int] = attr(name="BloodlustFrame", default=None)
    bonus_training_capacity: Optional[int] = attr(name="BonusTrainingCapacity", default=None)
    boost_level: Optional[int] = attr(name="BoostLevel", default=None)
    character_actions: List["entities.CharacterAction"] = wrapped("CharacterActions", element(tag="CharacterAction", default_factory=list))
    character_design_id: Optional[int] = attr(name="CharacterDesignId", default=None)
    character_id: Optional[int] = attr(name="CharacterId", default=None)
    character_name: Optional[str] = attr(name="CharacterName", default=None)
    deployment_date: Optional[datetime] = attr(name="DeploymentDate", default=None)
    designated_room_id: Optional[int] = attr(name="DesignatedRoomId", default=None)
    engine_improvement: Optional[int] = attr(name="EngineImprovement", default=None)
    fatigue: Optional[int] = attr(name="Fatigue", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    frame_to_attack_or_repair: Optional[int] = element("FrameToAttackOrRepair", default=None)
    hp_improvement: Optional[int] = attr(name="HpImprovement", default=None)
    invulnerability_frame: Optional[int] = attr(name="InvulnerabilityFrame", default=None)
    is_new: Optional[bool] = attr(name="IsNew", default=None)
    is_prestiging: Optional[bool] = element("IsPrestiging", default=None)
    item_ids: Optional[str] = attr(name="ItemIds", default=None)
    items: List["entities.Item"] = wrapped("Items", element(tag="Item", default_factory=list))
    level: Optional[int] = attr(name="Level", default=None)
    origin_room_id: Optional[int] = attr(name="OriginRoomId", default=None)
    owner_ship_id: Optional[int] = attr(name="OwnerShipId", default=None)
    owner_username: Optional[str] = attr(name="OwnerUsername", default=None)
    pilot_improvement: Optional[int] = attr(name="PilotImprovement", default=None)
    repair_improvement: Optional[int] = attr(name="RepairImprovement", default=None)
    room_id: Optional[int] = attr(name="RoomId", default=None)
    science_improvement: Optional[int] = attr(name="ScienceImprovement", default=None)
    ship_id: Optional[int] = attr(name="ShipId", default=None)
    skill_points: Optional[int] = attr(name="SkillPoints", default=None)
    stamina: Optional[int] = attr(name="Stamina", default=None)
    stamina_improvement: Optional[int] = attr(name="StaminaImprovement", default=None)
    target_room_id: Optional[int] = attr(name="TargetRoomId", default=None)
    training_data: Optional[str] = attr(name="TrainingData", default=None)
    training_design_id: Optional[int] = attr(name="TrainingDesignId", default=None)
    training_end_date: Optional[datetime] = attr(name="TrainingEndDate", default=None)
    weapon_improvement: Optional[int] = attr(name="WeaponImprovement", default=None)
    x_coordinate: Optional[int] = attr(name="XCoordinate", default=None)
    x_coordinate_ship_relative: Optional[int] = attr(name="XCoordinateShipRelative", default=None)
    xp: Optional[int] = attr(name="Xp", default=None)
    y_coordinate: Optional[int] = attr(name="YCoordinate", default=None)
    y_coordinate_ship_relative: Optional[int] = attr(name="YCoordinateShipRelative", default=None)

    def _key(self):
        return (
            self.ability_improvement,
            self.attack_improvement,
            self.available_date,
            self.battle_character_hp,
            self.bloodlust_frame,
            self.bonus_training_capacity,
            self.boost_level,
            tuple(child._key() for child in self.character_actions),
            self.character_design_id,
            self.character_id,
            self.character_name,
            self.deployment_date,
            self.designated_room_id,
            self.engine_improvement,
            self.fatigue,
            self.flags,
            self.hp_improvement,
            self.invulnerability_frame,
            self.is_new,
            self.item_ids,
            tuple(child._key() for child in self.items),
            self.level,
            self.origin_room_id,
            self.owner_ship_id,
            self.owner_username,
            self.pilot_improvement,
            self.repair_improvement,
            self.room_id,
            self.science_improvement,
            self.ship_id,
            self.skill_points,
            self.stamina,
            self.stamina_improvement,
            self.target_room_id,
            self.training_data,
            self.training_design_id,
            self.training_end_date,
            self.weapon_improvement,
            self.x_coordinate,
            self.x_coordinate_ship_relative,
            self.xp,
            self.y_coordinate,
            self.y_coordinate_ship_relative,
        )


__all__ = [
    "CharacterRaw",
]
