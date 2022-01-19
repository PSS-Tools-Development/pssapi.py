"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomDesignPurchaseRaw:
    XML_NODE_NAME: str = "RoomDesignPurchase"

    def __init__(self, room_design_purchase_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._availability_mask: int = _parse.pss_int(room_design_purchase_info.get("AvailabilityMask"))
        self._level: int = _parse.pss_int(room_design_purchase_info.get("Level"))
        self._quantity: int = _parse.pss_int(room_design_purchase_info.get("Quantity"))
        self._requirement_string: str = _parse.pss_str(room_design_purchase_info.get("RequirementString"))
        self._room_design_id: int = _parse.pss_int(room_design_purchase_info.get("RoomDesignId"))
        self._room_design_purchase_id: int = _parse.pss_int(room_design_purchase_info.get("RoomDesignPurchaseId"))

    @property
    def availability_mask(self) -> int:
        return self._availability_mask

    @property
    def level(self) -> int:
        return self._level

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def room_design_id(self) -> int:
        return self._room_design_id

    @property
    def room_design_purchase_id(self) -> int:
        return self._room_design_purchase_id

    def _key(self):
        return (
            self.availability_mask,
            self.level,
            self.quantity,
            self.requirement_string,
            self.room_design_id,
            self.room_design_purchase_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AvailabilityMask": self.availability_mask,
                "Level": self.level,
                "Quantity": self.quantity,
                "RequirementString": self.requirement_string,
                "RoomDesignId": self.room_design_id,
                "RoomDesignPurchaseId": self.room_design_purchase_id,
            }

        return self._dict
