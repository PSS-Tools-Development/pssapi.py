"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class CharacterDesignActionRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "CharacterDesignAction"

    def __init__(self, character_design_action_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._action_type_id: int = _parse.pss_int(character_design_action_info.pop("ActionTypeId", None))
        self._character_design_action_id: int = _parse.pss_int(character_design_action_info.pop("CharacterDesignActionId", None))
        self._character_design_action_index: int = _parse.pss_int(character_design_action_info.pop("CharacterDesignActionIndex", None))
        self._character_design_id: int = _parse.pss_int(character_design_action_info.pop("CharacterDesignId", None))
        self._condition_type_id: int = _parse.pss_int(character_design_action_info.pop("ConditionTypeId", None))
        super().__init__(character_design_action_info)

    @property
    def action_type_id(self) -> int:
        return self._action_type_id

    @property
    def character_design_action_id(self) -> int:
        return self._character_design_action_id

    @property
    def character_design_action_index(self) -> int:
        return self._character_design_action_index

    @property
    def character_design_id(self) -> int:
        return self._character_design_id

    @property
    def condition_type_id(self) -> int:
        return self._condition_type_id

    def _key(self):
        return (
            self.action_type_id,
            self.character_design_action_id,
            self.character_design_action_index,
            self.character_design_id,
            self.condition_type_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ActionTypeId": self.action_type_id,
                "CharacterDesignActionId": self.character_design_action_id,
                "CharacterDesignActionIndex": self.character_design_action_index,
                "CharacterDesignId": self.character_design_id,
                "ConditionTypeId": self.condition_type_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
