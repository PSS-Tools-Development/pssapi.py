"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ItemDesignActionRaw:
    XML_NODE_NAME: str = "ItemDesignAction"

    def __init__(self, item_design_action_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._action_type_id: int = _parse.pss_int(item_design_action_info.get("ActionTypeId"))
        self._condition_type_id: int = _parse.pss_int(item_design_action_info.get("ConditionTypeId"))
        self._item_design_action_id: int = _parse.pss_int(item_design_action_info.get("ItemDesignActionId"))
        self._item_design_action_index: int = _parse.pss_int(item_design_action_info.get("ItemDesignActionIndex"))
        self._item_design_id: int = _parse.pss_int(item_design_action_info.get("ItemDesignId"))

    @property
    def action_type_id(self) -> int:
        return self._action_type_id

    @property
    def condition_type_id(self) -> int:
        return self._condition_type_id

    @property
    def item_design_action_id(self) -> int:
        return self._item_design_action_id

    @property
    def item_design_action_index(self) -> int:
        return self._item_design_action_index

    @property
    def item_design_id(self) -> int:
        return self._item_design_id

    def _key(self):
        return (
            self.action_type_id,
            self.condition_type_id,
            self.item_design_action_id,
            self.item_design_action_index,
            self.item_design_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ActionTypeId": self.action_type_id,
                "ConditionTypeId": self.condition_type_id,
                "ItemDesignActionId": self.item_design_action_id,
                "ItemDesignActionIndex": self.item_design_action_index,
                "ItemDesignId": self.item_design_id,
            }

        return self._dict
