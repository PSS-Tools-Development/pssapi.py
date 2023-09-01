"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict
from typing import List as _List

import pssapi.entities as _entities

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterRaw:
    XML_NODE_NAME: str = "Character"

    def __init__(self, character_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._ability_improvement: int = _parse.pss_int(character_info.get("AbilityImprovement"))
        self._attack_improvement: int = _parse.pss_int(character_info.get("AttackImprovement"))
        self._available_date: _datetime = _parse.pss_datetime(character_info.get("AvailableDate"))
        self._battle_character_hp: int = _parse.pss_int(character_info.get("BattleCharacterHp"))
        self._bloodlust_frame: int = _parse.pss_int(character_info.get("BloodlustFrame"))
        self._character_actions: _List[_entities.CharacterAction] = (
            [_entities.CharacterAction(child_info) for child_info in character_info.get("CharacterActions")] if character_info.get("CharacterActions") else []
        )
        self._character_design_id: int = _parse.pss_int(character_info.get("CharacterDesignId"))
        self._character_id: int = _parse.pss_int(character_info.get("CharacterId"))
        self._character_name: str = _parse.pss_str(character_info.get("CharacterName"))
        self._deployment_date: _datetime = _parse.pss_datetime(character_info.get("DeploymentDate"))
        self._designated_room_id: int = _parse.pss_int(character_info.get("DesignatedRoomId"))
        self._engine_improvement: int = _parse.pss_int(character_info.get("EngineImprovement"))
        self._fatigue: int = _parse.pss_int(character_info.get("Fatigue"))
        self._flags: int = _parse.pss_int(character_info.get("Flags"))
        self._hp_improvement: int = _parse.pss_int(character_info.get("HpImprovement"))
        self._invulnerability_frame: int = _parse.pss_int(character_info.get("InvulnerabilityFrame"))
        self._is_new: bool = _parse.pss_bool(character_info.get("IsNew"))
        self._item_ids: str = _parse.pss_str(character_info.get("ItemIds"))
        self._items: _List[_entities.Item] = [_entities.Item(child_info) for child_info in character_info.get("Items")] if character_info.get("Items") else []
        self._level: int = _parse.pss_int(character_info.get("Level"))
        self._origin_room_id: int = _parse.pss_int(character_info.get("OriginRoomId"))
        self._owner_ship_id: int = _parse.pss_int(character_info.get("OwnerShipId"))
        self._owner_username: str = _parse.pss_str(character_info.get("OwnerUsername"))
        self._pilot_improvement: int = _parse.pss_int(character_info.get("PilotImprovement"))
        self._repair_improvement: int = _parse.pss_int(character_info.get("RepairImprovement"))
        self._room_id: int = _parse.pss_int(character_info.get("RoomId"))
        self._science_improvement: int = _parse.pss_int(character_info.get("ScienceImprovement"))
        self._ship_id: int = _parse.pss_int(character_info.get("ShipId"))
        self._skill_points: int = _parse.pss_int(character_info.get("SkillPoints"))
        self._stamina: int = _parse.pss_int(character_info.get("Stamina"))
        self._stamina_improvement: int = _parse.pss_int(character_info.get("StaminaImprovement"))
        self._target_room_id: int = _parse.pss_int(character_info.get("TargetRoomId"))
        self._training_data: str = _parse.pss_str(character_info.get("TrainingData"))
        self._training_design_id: int = _parse.pss_int(character_info.get("TrainingDesignId"))
        self._training_end_date: _datetime = _parse.pss_datetime(character_info.get("TrainingEndDate"))
        self._weapon_improvement: int = _parse.pss_int(character_info.get("WeaponImprovement"))
        self._x_coordinate: int = _parse.pss_int(character_info.get("XCoordinate"))
        self._x_coordinate_ship_relative: int = _parse.pss_int(character_info.get("XCoordinateShipRelative"))
        self._xp: int = _parse.pss_int(character_info.get("Xp"))
        self._y_coordinate: int = _parse.pss_int(character_info.get("YCoordinate"))
        self._y_coordinate_ship_relative: int = _parse.pss_int(character_info.get("YCoordinateShipRelative"))

    @property
    def ability_improvement(self) -> int:
        return self._ability_improvement

    @property
    def attack_improvement(self) -> int:
        return self._attack_improvement

    @property
    def available_date(self) -> _datetime:
        return self._available_date

    @property
    def battle_character_hp(self) -> int:
        return self._battle_character_hp

    @property
    def bloodlust_frame(self) -> int:
        return self._bloodlust_frame

    @property
    def character_actions(self) -> _List["_entities.CharacterAction"]:
        return self._character_actions

    @property
    def character_design_id(self) -> int:
        return self._character_design_id

    @property
    def character_id(self) -> int:
        return self._character_id

    @property
    def character_name(self) -> str:
        return self._character_name

    @property
    def deployment_date(self) -> _datetime:
        return self._deployment_date

    @property
    def designated_room_id(self) -> int:
        return self._designated_room_id

    @property
    def engine_improvement(self) -> int:
        return self._engine_improvement

    @property
    def fatigue(self) -> int:
        return self._fatigue

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def hp_improvement(self) -> int:
        return self._hp_improvement

    @property
    def invulnerability_frame(self) -> int:
        return self._invulnerability_frame

    @property
    def is_new(self) -> bool:
        return self._is_new

    @property
    def item_ids(self) -> str:
        return self._item_ids

    @property
    def items(self) -> _List["_entities.Item"]:
        return self._items

    @property
    def level(self) -> int:
        return self._level

    @property
    def origin_room_id(self) -> int:
        return self._origin_room_id

    @property
    def owner_ship_id(self) -> int:
        return self._owner_ship_id

    @property
    def owner_username(self) -> str:
        return self._owner_username

    @property
    def pilot_improvement(self) -> int:
        return self._pilot_improvement

    @property
    def repair_improvement(self) -> int:
        return self._repair_improvement

    @property
    def room_id(self) -> int:
        return self._room_id

    @property
    def science_improvement(self) -> int:
        return self._science_improvement

    @property
    def ship_id(self) -> int:
        return self._ship_id

    @property
    def skill_points(self) -> int:
        return self._skill_points

    @property
    def stamina(self) -> int:
        return self._stamina

    @property
    def stamina_improvement(self) -> int:
        return self._stamina_improvement

    @property
    def target_room_id(self) -> int:
        return self._target_room_id

    @property
    def training_data(self) -> str:
        return self._training_data

    @property
    def training_design_id(self) -> int:
        return self._training_design_id

    @property
    def training_end_date(self) -> _datetime:
        return self._training_end_date

    @property
    def weapon_improvement(self) -> int:
        return self._weapon_improvement

    @property
    def x_coordinate(self) -> int:
        return self._x_coordinate

    @property
    def x_coordinate_ship_relative(self) -> int:
        return self._x_coordinate_ship_relative

    @property
    def xp(self) -> int:
        return self._xp

    @property
    def y_coordinate(self) -> int:
        return self._y_coordinate

    @property
    def y_coordinate_ship_relative(self) -> int:
        return self._y_coordinate_ship_relative

    def _key(self):
        return (
            self.ability_improvement,
            self.attack_improvement,
            self.available_date,
            self.battle_character_hp,
            self.bloodlust_frame,
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

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AbilityImprovement": self.ability_improvement,
                "AttackImprovement": self.attack_improvement,
                "AvailableDate": self.available_date,
                "BattleCharacterHp": self.battle_character_hp,
                "BloodlustFrame": self.bloodlust_frame,
                "CharacterActions": [dict(child) for child in self.character_actions],
                "CharacterDesignId": self.character_design_id,
                "CharacterId": self.character_id,
                "CharacterName": self.character_name,
                "DeploymentDate": self.deployment_date,
                "DesignatedRoomId": self.designated_room_id,
                "EngineImprovement": self.engine_improvement,
                "Fatigue": self.fatigue,
                "Flags": self.flags,
                "HpImprovement": self.hp_improvement,
                "InvulnerabilityFrame": self.invulnerability_frame,
                "IsNew": self.is_new,
                "ItemIds": self.item_ids,
                "Items": [dict(child) for child in self.items],
                "Level": self.level,
                "OriginRoomId": self.origin_room_id,
                "OwnerShipId": self.owner_ship_id,
                "OwnerUsername": self.owner_username,
                "PilotImprovement": self.pilot_improvement,
                "RepairImprovement": self.repair_improvement,
                "RoomId": self.room_id,
                "ScienceImprovement": self.science_improvement,
                "ShipId": self.ship_id,
                "SkillPoints": self.skill_points,
                "Stamina": self.stamina,
                "StaminaImprovement": self.stamina_improvement,
                "TargetRoomId": self.target_room_id,
                "TrainingData": self.training_data,
                "TrainingDesignId": self.training_design_id,
                "TrainingEndDate": self.training_end_date,
                "WeaponImprovement": self.weapon_improvement,
                "XCoordinate": self.x_coordinate,
                "XCoordinateShipRelative": self.x_coordinate_ship_relative,
                "Xp": self.xp,
                "YCoordinate": self.y_coordinate,
                "YCoordinateShipRelative": self.y_coordinate_ship_relative,
            }

        return self._dict
