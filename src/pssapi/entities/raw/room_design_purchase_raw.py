"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw


class RoomDesignPurchaseRaw(EntityBaseRaw):
    XML_NODE_NAME: str = "RoomDesignPurchase"

    def __init__(self, room_design_purchase_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._availability_mask: int = _parse.pss_int(room_design_purchase_info.pop("AvailabilityMask", None))
        self._level: int = _parse.pss_int(room_design_purchase_info.pop("Level", None))
        self._quantity: int = _parse.pss_int(room_design_purchase_info.pop("Quantity", None))
        self._requirement_string: str = _parse.pss_str(room_design_purchase_info.pop("RequirementString", None))
        self._room_design_id: int = _parse.pss_int(room_design_purchase_info.pop("RoomDesignId", None))
        self._room_design_purchase_id: int = _parse.pss_int(room_design_purchase_info.pop("RoomDesignPurchaseId", None))
        super().__init__(room_design_purchase_info)

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
            self._dict.update(super().__dict__())

        return self._dict
