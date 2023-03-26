"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ItemRaw:
    XML_NODE_NAME: str = "Item"

    def __init__(self, item_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._bonus_enhancement_type: str = _parse.pss_str(item_info.get("BonusEnhancementType"))
        self._bonus_enhancement_value: str = _parse.pss_str(item_info.get("BonusEnhancementValue"))
        self._is_new: bool = _parse.pss_bool(item_info.get("IsNew"))
        self._item_design_id: int = _parse.pss_int(item_info.get("ItemDesignId"))
        self._item_id: int = _parse.pss_int(item_info.get("ItemId"))
        self._quantity: int = _parse.pss_int(item_info.get("Quantity"))
        self._ship_id: int = _parse.pss_int(item_info.get("ShipId"))

    @property
    def bonus_enhancement_type(self) -> str:
        return self._bonus_enhancement_type

    @property
    def bonus_enhancement_value(self) -> str:
        return self._bonus_enhancement_value

    @property
    def is_new(self) -> bool:
        return self._is_new

    @property
    def item_design_id(self) -> int:
        return self._item_design_id

    @property
    def item_id(self) -> int:
        return self._item_id

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def ship_id(self) -> int:
        return self._ship_id

    def _key(self):
        return (
            self.bonus_enhancement_type,
            self.bonus_enhancement_value,
            self.is_new,
            self.item_design_id,
            self.item_id,
            self.quantity,
            self.ship_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BonusEnhancementType": self.bonus_enhancement_type,
                "BonusEnhancementValue": self.bonus_enhancement_value,
                "IsNew": self.is_new,
                "ItemDesignId": self.item_design_id,
                "ItemId": self.item_id,
                "Quantity": self.quantity,
                "ShipId": self.ship_id,
            }

        return self._dict
