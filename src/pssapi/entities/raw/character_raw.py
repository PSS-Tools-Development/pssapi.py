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
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class CharacterRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Character"

    def __init__(self, character_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._ability_improvement: int = _parse.pss_int(character_info.pop("AbilityImprovement", None))
        self._attack_improvement: int = _parse.pss_int(character_info.pop("AttackImprovement", None))
        self._available_date: _datetime = _parse.pss_datetime(character_info.pop("AvailableDate", None))
        self._battle_character_hp: int = _parse.pss_int(character_info.pop("BattleCharacterHp", None))
        self._bloodlust_frame: int = _parse.pss_int(character_info.pop("BloodlustFrame", None))
        self._character_actions: _List[_entities.CharacterAction] = (
            [_entities.CharacterAction(child_info) for child_info in character_info.pop("CharacterActions")[0].get("CharacterAction", [])] if character_info.get("CharacterActions") else []
        )
        self._character_design_id: int = _parse.pss_int(character_info.pop("CharacterDesignId", None))
        self._character_id: int = _parse.pss_int(character_info.pop("CharacterId", None))
        self._character_name: str = _parse.pss_str(character_info.pop("CharacterName", None))
        self._deployment_date: _datetime = _parse.pss_datetime(character_info.pop("DeploymentDate", None))
        self._designated_room_id: int = _parse.pss_int(character_info.pop("DesignatedRoomId", None))
        self._engine_improvement: int = _parse.pss_int(character_info.pop("EngineImprovement", None))
        self._fatigue: int = _parse.pss_int(character_info.pop("Fatigue", None))
        self._flags: int = _parse.pss_int(character_info.pop("Flags", None))
        self._hp_improvement: int = _parse.pss_int(character_info.pop("HpImprovement", None))
        self._invulnerability_frame: int = _parse.pss_int(character_info.pop("InvulnerabilityFrame", None))
        self._is_new: bool = _parse.pss_bool(character_info.pop("IsNew", None))
        self._item_ids: str = _parse.pss_str(character_info.pop("ItemIds", None))
        self._items: _List[_entities.Item] = [_entities.Item(child_info) for child_info in character_info.pop("Items")[0].get("Item", [])] if character_info.get("Items") else []
        self._level: int = _parse.pss_int(character_info.pop("Level", None))
        self._origin_room_id: int = _parse.pss_int(character_info.pop("OriginRoomId", None))
        self._owner_ship_id: int = _parse.pss_int(character_info.pop("OwnerShipId", None))
        self._owner_username: str = _parse.pss_str(character_info.pop("OwnerUsername", None))
        self._pilot_improvement: int = _parse.pss_int(character_info.pop("PilotImprovement", None))
        self._repair_improvement: int = _parse.pss_int(character_info.pop("RepairImprovement", None))
        self._room_id: int = _parse.pss_int(character_info.pop("RoomId", None))
        self._science_improvement: int = _parse.pss_int(character_info.pop("ScienceImprovement", None))
        self._ship_id: int = _parse.pss_int(character_info.pop("ShipId", None))
        self._skill_points: int = _parse.pss_int(character_info.pop("SkillPoints", None))
        self._stamina: int = _parse.pss_int(character_info.pop("Stamina", None))
        self._stamina_improvement: int = _parse.pss_int(character_info.pop("StaminaImprovement", None))
        self._target_room_id: int = _parse.pss_int(character_info.pop("TargetRoomId", None))
        self._training_data: str = _parse.pss_str(character_info.pop("TrainingData", None))
        self._training_design_id: int = _parse.pss_int(character_info.pop("TrainingDesignId", None))
        self._training_end_date: _datetime = _parse.pss_datetime(character_info.pop("TrainingEndDate", None))
        self._weapon_improvement: int = _parse.pss_int(character_info.pop("WeaponImprovement", None))
        self._x_coordinate: int = _parse.pss_int(character_info.pop("XCoordinate", None))
        self._x_coordinate_ship_relative: int = _parse.pss_int(character_info.pop("XCoordinateShipRelative", None))
        self._xp: int = _parse.pss_int(character_info.pop("Xp", None))
        self._y_coordinate: int = _parse.pss_int(character_info.pop("YCoordinate", None))
        self._y_coordinate_ship_relative: int = _parse.pss_int(character_info.pop("YCoordinateShipRelative", None))
        super().__init__(character_info)

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
            self._dict.update(super().__dict__())

        return self._dict
