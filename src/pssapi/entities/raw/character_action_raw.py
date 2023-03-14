"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterActionRaw:
    XML_NODE_NAME: str = "CharacterAction"

    def __init__(self, character_action_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._action_type_id: int = _parse.pss_int(character_action_info.get("ActionTypeId"))
        self._character_action_id: int = _parse.pss_int(character_action_info.get("CharacterActionId"))
        self._character_action_index: int = _parse.pss_int(character_action_info.get("CharacterActionIndex"))
        self._character_id: int = _parse.pss_int(character_action_info.get("CharacterId"))
        self._condition_type_id: int = _parse.pss_int(character_action_info.get("ConditionTypeId"))

    @property
    def action_type_id(self) -> int:
        return self._action_type_id

    @property
    def character_action_id(self) -> int:
        return self._character_action_id

    @property
    def character_action_index(self) -> int:
        return self._character_action_index

    @property
    def character_id(self) -> int:
        return self._character_id

    @property
    def condition_type_id(self) -> int:
        return self._condition_type_id

    def _key(self):
        return (
            self.action_type_id,
            self.character_action_id,
            self.character_action_index,
            self.character_id,
            self.condition_type_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ActionTypeId": self.action_type_id,
                "CharacterActionId": self.character_action_id,
                "CharacterActionIndex": self.character_action_index,
                "CharacterId": self.character_id,
                "ConditionTypeId": self.condition_type_id,
            }

        return self._dict
