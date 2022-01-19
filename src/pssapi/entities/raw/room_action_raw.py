"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomActionRaw:
    XML_NODE_NAME: str = "RoomAction"

    def __init__(self, room_action_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._action_type_id: int = _parse.pss_int(room_action_info.get("ActionTypeId"))
        self._condition_type_id: int = _parse.pss_int(room_action_info.get("ConditionTypeId"))
        self._room_action_id: int = _parse.pss_int(room_action_info.get("RoomActionId"))
        self._room_action_index: int = _parse.pss_int(room_action_info.get("RoomActionIndex"))
        self._room_id: int = _parse.pss_int(room_action_info.get("RoomId"))

    @property
    def action_type_id(self) -> int:
        return self._action_type_id

    @property
    def condition_type_id(self) -> int:
        return self._condition_type_id

    @property
    def room_action_id(self) -> int:
        return self._room_action_id

    @property
    def room_action_index(self) -> int:
        return self._room_action_index

    @property
    def room_id(self) -> int:
        return self._room_id

    def _key(self):
        return (
            self.action_type_id,
            self.condition_type_id,
            self.room_action_id,
            self.room_action_index,
            self.room_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ActionTypeId": self.action_type_id,
                "ConditionTypeId": self.condition_type_id,
                "RoomActionId": self.room_action_id,
                "RoomActionIndex": self.room_action_index,
                "RoomId": self.room_id,
            }

        return self._dict
