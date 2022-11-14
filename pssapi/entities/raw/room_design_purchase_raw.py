"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomDesignPurchaseRaw:
    XML_NODE_NAME: str = 'RoomDesignPurchase'

    def __init__(self, room_design_purchase_info: _EntityInfo) -> None:
        self.availability_mask: int = _parse.pss_int(room_design_purchase_info.get('AvailabilityMask'))
        self.level: int = _parse.pss_int(room_design_purchase_info.get('Level'))
        self.quantity: int = _parse.pss_int(room_design_purchase_info.get('Quantity'))
        self.requirement_string: str = _parse.pss_str(room_design_purchase_info.get('RequirementString'))
        self.room_design_id: int = _parse.pss_int(room_design_purchase_info.get('RoomDesignId'))
        self.room_design_purchase_id: int = _parse.pss_int(room_design_purchase_info.get('RoomDesignPurchaseId'))
