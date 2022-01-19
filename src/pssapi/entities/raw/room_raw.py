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


class RoomRaw:
    XML_NODE_NAME: str = "Room"

    def __init__(self, room_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._capacity_used: int = _parse.pss_int(room_info.get("CapacityUsed"))
        self._column: int = _parse.pss_int(room_info.get("Column"))
        self._construction_start_date: _datetime = _parse.pss_datetime(room_info.get("ConstructionStartDate"))
        self._current_skin_key: int = _parse.pss_int(room_info.get("CurrentSkinKey"))
        self._item_ids: str = _parse.pss_str(room_info.get("ItemIds"))
        self._manufacture_start_date: _datetime = _parse.pss_datetime(room_info.get("ManufactureStartDate"))
        self._manufacture_string: str = _parse.pss_str(room_info.get("ManufactureString"))
        self._manufactured: int = _parse.pss_int(room_info.get("Manufactured"))
        self._power_generated: int = _parse.pss_int(room_info.get("PowerGenerated"))
        self._previous_skin_key: int = _parse.pss_int(room_info.get("PreviousSkinKey"))
        self._random_seed: int = _parse.pss_int(room_info.get("RandomSeed"))
        self._room_actions: _List[_entities.RoomAction] = [_entities.RoomAction(child_info) for child_info in room_info.get("RoomActions")] if room_info.get("RoomActions") else []
        self._room_design_id: int = _parse.pss_int(room_info.get("RoomDesignId"))
        self._room_id: int = _parse.pss_int(room_info.get("RoomId"))
        self._room_status: str = _parse.pss_str(room_info.get("RoomStatus"))
        self._row: int = _parse.pss_int(room_info.get("Row"))
        self._salvage_string: str = _parse.pss_str(room_info.get("SalvageString"))
        self._ship_id: int = _parse.pss_int(room_info.get("ShipId"))
        self._target_manufacture_string: str = _parse.pss_str(room_info.get("TargetManufactureString"))
        self._upgrade_room_design_id: int = _parse.pss_int(room_info.get("UpgradeRoomDesignId"))

    @property
    def capacity_used(self) -> int:
        return self._capacity_used

    @property
    def column(self) -> int:
        return self._column

    @property
    def construction_start_date(self) -> _datetime:
        return self._construction_start_date

    @property
    def current_skin_key(self) -> int:
        return self._current_skin_key

    @property
    def item_ids(self) -> str:
        return self._item_ids

    @property
    def manufacture_start_date(self) -> _datetime:
        return self._manufacture_start_date

    @property
    def manufacture_string(self) -> str:
        return self._manufacture_string

    @property
    def manufactured(self) -> int:
        return self._manufactured

    @property
    def power_generated(self) -> int:
        return self._power_generated

    @property
    def previous_skin_key(self) -> int:
        return self._previous_skin_key

    @property
    def random_seed(self) -> int:
        return self._random_seed

    @property
    def room_actions(self) -> _List["_entities.RoomAction"]:
        return self._room_actions

    @property
    def room_design_id(self) -> int:
        return self._room_design_id

    @property
    def room_id(self) -> int:
        return self._room_id

    @property
    def room_status(self) -> str:
        return self._room_status

    @property
    def row(self) -> int:
        return self._row

    @property
    def salvage_string(self) -> str:
        return self._salvage_string

    @property
    def ship_id(self) -> int:
        return self._ship_id

    @property
    def target_manufacture_string(self) -> str:
        return self._target_manufacture_string

    @property
    def upgrade_room_design_id(self) -> int:
        return self._upgrade_room_design_id

    def _key(self):
        return (
            self.capacity_used,
            self.column,
            self.construction_start_date,
            self.current_skin_key,
            self.item_ids,
            self.manufacture_start_date,
            self.manufacture_string,
            self.manufactured,
            self.power_generated,
            self.previous_skin_key,
            self.random_seed,
            tuple(child._key() for child in self.room_actions),
            self.room_design_id,
            self.room_id,
            self.room_status,
            self.row,
            self.salvage_string,
            self.ship_id,
            self.target_manufacture_string,
            self.upgrade_room_design_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "CapacityUsed": self.capacity_used,
                "Column": self.column,
                "ConstructionStartDate": self.construction_start_date,
                "CurrentSkinKey": self.current_skin_key,
                "ItemIds": self.item_ids,
                "ManufactureStartDate": self.manufacture_start_date,
                "ManufactureString": self.manufacture_string,
                "Manufactured": self.manufactured,
                "PowerGenerated": self.power_generated,
                "PreviousSkinKey": self.previous_skin_key,
                "RandomSeed": self.random_seed,
                "RoomActions": [dict(child) for child in self.room_actions],
                "RoomDesignId": self.room_design_id,
                "RoomId": self.room_id,
                "RoomStatus": self.room_status,
                "Row": self.row,
                "SalvageString": self.salvage_string,
                "ShipId": self.ship_id,
                "TargetManufactureString": self.target_manufacture_string,
                "UpgradeRoomDesignId": self.upgrade_room_design_id,
            }

        return self._dict
