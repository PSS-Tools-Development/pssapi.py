"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomDesignPurchaseRaw:
    XML_NODE_NAME: str = 'RoomDesignPurchase'

    def __init__(self, room_design_purchase_info: _EntityInfo) -> None:
        self.__room_design_purchase_id: int = _parse.pss_int(
            room_design_purchase_info.get('RoomDesignPurchaseId'))
        self.__room_design_id: int = _parse.pss_int(
            room_design_purchase_info.get('RoomDesignId'))
        self.__level: int = _parse.pss_int(
            room_design_purchase_info.get('Level'))
        self.__quantity: int = _parse.pss_int(
            room_design_purchase_info.get('Quantity'))
        self.__availability_mask: int = _parse.pss_int(
            room_design_purchase_info.get('AvailabilityMask'))
        self.__requirement_string: str = _parse.pss_str(
            room_design_purchase_info.get('RequirementString'))

    @property
    def room_design_purchase_id(self) -> int:
        return self.__room_design_purchase_id

    @property
    def room_design_id(self) -> int:
        return self.__room_design_id

    @property
    def level(self) -> int:
        return self.__level

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def availability_mask(self) -> int:
        return self.__availability_mask

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string
