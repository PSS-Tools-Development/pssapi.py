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


class RoomRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Room"

    def __init__(self, room_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._assigned_power: int = _parse.pss_int(room_info.pop("AssignedPower", None))
        self._capacity_used: int = _parse.pss_int(room_info.pop("CapacityUsed", None))
        self._center_x: int = _parse.pss_int(room_info.pop("CenterX", None))
        self._center_y: int = _parse.pss_int(room_info.pop("CenterY", None))
        self._column: int = _parse.pss_int(room_info.pop("Column", None))
        self._construction_start_date: _datetime = _parse.pss_datetime(room_info.pop("ConstructionStartDate", None))
        self._current_capacity: int = _parse.pss_int(room_info.pop("CurrentCapacity", None))
        self._current_skin_key: int = _parse.pss_int(room_info.pop("CurrentSkinKey", None))
        self._disable_count: int = _parse.pss_int(room_info.pop("DisableCount", None))
        self._is_power_ai_active: bool = _parse.pss_bool(room_info.pop("IsPowerAIActive", None))
        self._is_set_item_ai_active: bool = _parse.pss_bool(room_info.pop("IsSetItemAIActive", None))
        self._is_target_ai_active: bool = _parse.pss_bool(room_info.pop("IsTargetAIActive", None))
        self._item_ids: str = _parse.pss_str(room_info.pop("ItemIds", None))
        self._item_skin_key: int = _parse.pss_int(room_info.pop("ItemSkinKey", None))
        self._local_center_x: int = _parse.pss_int(room_info.pop("LocalCenterX", None))
        self._local_center_y: int = _parse.pss_int(room_info.pop("LocalCenterY", None))
        self._manufacture_start_date: _datetime = _parse.pss_datetime(room_info.pop("ManufactureStartDate", None))
        self._manufacture_string: str = _parse.pss_str(room_info.pop("ManufactureString", None))
        self._manufactured: int = _parse.pss_int(room_info.pop("Manufactured", None))
        self._power_generated: int = _parse.pss_int(room_info.pop("PowerGenerated", None))
        self._previous_skin_key: int = _parse.pss_int(room_info.pop("PreviousSkinKey", None))
        self._progress: int = _parse.pss_int(room_info.pop("Progress", None))
        self._protect_room_frame: int = _parse.pss_int(room_info.pop("ProtectRoomFrame", None))
        self._random_seed: int = _parse.pss_int(room_info.pop("RandomSeed", None))
        self._room_actions: _List[_entities.RoomAction] = (
            [_entities.RoomAction(child_info) for child_info in room_info.pop("RoomActions")[0].get("RoomAction", [])] if room_info.get("RoomActions") else []
        )
        self._room_design_id: int = _parse.pss_int(room_info.pop("RoomDesignId", None))
        self._room_id: int = _parse.pss_int(room_info.pop("RoomId", None))
        self._room_status: str = _parse.pss_str(room_info.pop("RoomStatus", None))
        self._row: int = _parse.pss_int(room_info.pop("Row", None))
        self._run_room_action: bool = _parse.pss_bool(room_info.pop("RunRoomAction", None))
        self._salvage_string: str = _parse.pss_str(room_info.pop("SalvageString", None))
        self._ship_id: int = _parse.pss_int(room_info.pop("ShipId", None))
        self._skin_key: int = _parse.pss_int(room_info.pop("SkinKey", None))
        self._system_power: int = _parse.pss_int(room_info.pop("SystemPower", None))
        self._target_craft_id: int = _parse.pss_int(room_info.pop("TargetCraftId", None))
        self._target_manufacture_string: str = _parse.pss_str(room_info.pop("TargetManufactureString", None))
        self._target_room_id: int = _parse.pss_int(room_info.pop("TargetRoomId", None))
        self._top_left_x: int = _parse.pss_int(room_info.pop("TopLeftX", None))
        self._top_left_y: int = _parse.pss_int(room_info.pop("TopLeftY", None))
        self._total_damage: int = _parse.pss_int(room_info.pop("TotalDamage", None))
        self._upgrade_room_design_id: int = _parse.pss_int(room_info.pop("UpgradeRoomDesignId", None))
        super().__init__(room_info)

    @property
    def assigned_power(self) -> int:
        return self._assigned_power

    @property
    def capacity_used(self) -> int:
        return self._capacity_used

    @property
    def center_x(self) -> int:
        return self._center_x

    @property
    def center_y(self) -> int:
        return self._center_y

    @property
    def column(self) -> int:
        return self._column

    @property
    def construction_start_date(self) -> _datetime:
        return self._construction_start_date

    @property
    def current_capacity(self) -> int:
        return self._current_capacity

    @property
    def current_skin_key(self) -> int:
        return self._current_skin_key

    @property
    def disable_count(self) -> int:
        return self._disable_count

    @property
    def is_power_ai_active(self) -> bool:
        return self._is_power_ai_active

    @property
    def is_set_item_ai_active(self) -> bool:
        return self._is_set_item_ai_active

    @property
    def is_target_ai_active(self) -> bool:
        return self._is_target_ai_active

    @property
    def item_ids(self) -> str:
        return self._item_ids

    @property
    def item_skin_key(self) -> int:
        return self._item_skin_key

    @property
    def local_center_x(self) -> int:
        return self._local_center_x

    @property
    def local_center_y(self) -> int:
        return self._local_center_y

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
    def progress(self) -> int:
        return self._progress

    @property
    def protect_room_frame(self) -> int:
        return self._protect_room_frame

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
    def run_room_action(self) -> bool:
        return self._run_room_action

    @property
    def salvage_string(self) -> str:
        return self._salvage_string

    @property
    def ship_id(self) -> int:
        return self._ship_id

    @property
    def skin_key(self) -> int:
        return self._skin_key

    @property
    def system_power(self) -> int:
        return self._system_power

    @property
    def target_craft_id(self) -> int:
        return self._target_craft_id

    @property
    def target_manufacture_string(self) -> str:
        return self._target_manufacture_string

    @property
    def target_room_id(self) -> int:
        return self._target_room_id

    @property
    def top_left_x(self) -> int:
        return self._top_left_x

    @property
    def top_left_y(self) -> int:
        return self._top_left_y

    @property
    def total_damage(self) -> int:
        return self._total_damage

    @property
    def upgrade_room_design_id(self) -> int:
        return self._upgrade_room_design_id

    def _key(self):
        return (
            self.assigned_power,
            self.capacity_used,
            self.center_x,
            self.center_y,
            self.column,
            self.construction_start_date,
            self.current_capacity,
            self.current_skin_key,
            self.disable_count,
            self.is_power_ai_active,
            self.is_set_item_ai_active,
            self.is_target_ai_active,
            self.item_ids,
            self.item_skin_key,
            self.local_center_x,
            self.local_center_y,
            self.manufacture_start_date,
            self.manufacture_string,
            self.manufactured,
            self.power_generated,
            self.previous_skin_key,
            self.progress,
            self.protect_room_frame,
            self.random_seed,
            tuple(child._key() for child in self.room_actions),
            self.room_design_id,
            self.room_id,
            self.room_status,
            self.row,
            self.run_room_action,
            self.salvage_string,
            self.ship_id,
            self.skin_key,
            self.system_power,
            self.target_craft_id,
            self.target_manufacture_string,
            self.target_room_id,
            self.top_left_x,
            self.top_left_y,
            self.total_damage,
            self.upgrade_room_design_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AssignedPower": self.assigned_power,
                "CapacityUsed": self.capacity_used,
                "CenterX": self.center_x,
                "CenterY": self.center_y,
                "Column": self.column,
                "ConstructionStartDate": self.construction_start_date,
                "CurrentCapacity": self.current_capacity,
                "CurrentSkinKey": self.current_skin_key,
                "DisableCount": self.disable_count,
                "IsPowerAIActive": self.is_power_ai_active,
                "IsSetItemAIActive": self.is_set_item_ai_active,
                "IsTargetAIActive": self.is_target_ai_active,
                "ItemIds": self.item_ids,
                "ItemSkinKey": self.item_skin_key,
                "LocalCenterX": self.local_center_x,
                "LocalCenterY": self.local_center_y,
                "ManufactureStartDate": self.manufacture_start_date,
                "ManufactureString": self.manufacture_string,
                "Manufactured": self.manufactured,
                "PowerGenerated": self.power_generated,
                "PreviousSkinKey": self.previous_skin_key,
                "Progress": self.progress,
                "ProtectRoomFrame": self.protect_room_frame,
                "RandomSeed": self.random_seed,
                "RoomActions": [dict(child) for child in self.room_actions],
                "RoomDesignId": self.room_design_id,
                "RoomId": self.room_id,
                "RoomStatus": self.room_status,
                "Row": self.row,
                "RunRoomAction": self.run_room_action,
                "SalvageString": self.salvage_string,
                "ShipId": self.ship_id,
                "SkinKey": self.skin_key,
                "SystemPower": self.system_power,
                "TargetCraftId": self.target_craft_id,
                "TargetManufactureString": self.target_manufacture_string,
                "TargetRoomId": self.target_room_id,
                "TopLeftX": self.top_left_x,
                "TopLeftY": self.top_left_y,
                "TotalDamage": self.total_damage,
                "UpgradeRoomDesignId": self.upgrade_room_design_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
