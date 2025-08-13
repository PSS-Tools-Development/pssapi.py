"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class RoomDesignPurchaseRaw(EntityBaseRaw, tag="RoomDesignPurchase"):
    XML_NODE_NAME: str = "RoomDesignPurchase"

    availability_mask: Optional[int] = attr(name="AvailabilityMask", default=None)
    level: Optional[int] = attr(name="Level", default=None)
    quantity: Optional[int] = attr(name="Quantity", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    room_design_id: Optional[int] = attr(name="RoomDesignId", default=None)
    room_design_purchase_id: Optional[int] = attr(name="RoomDesignPurchaseId", default=None)

    def _key(self):
        return (
            self.availability_mask,
            self.level,
            self.quantity,
            self.requirement_string,
            self.room_design_id,
            self.room_design_purchase_id,
        )


__all__ = [
    "RoomDesignPurchaseRaw",
]
