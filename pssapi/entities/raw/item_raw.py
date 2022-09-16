####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ItemRaw():
    XML_NODE_NAME: str = 'Item'

    def __init__(self, item_info: _EntityInfo) -> None:
        self.__item_design_id: int = _parse.pss_int(item_info.get('ItemDesignId'))
        self.__bonus_enhancement_value: float = _parse.pss_float(item_info.get('BonusEnhancementValue'))
        self.__ship_id: int = _parse.pss_int(item_info.get('ShipId'))
        self.__quantity: int = _parse.pss_int(item_info.get('Quantity'))
        self.__is_new: bool = _parse.pss_bool(item_info.get('IsNew'))
        self.__bonus_enhancement_type: str = _parse.pss_str(item_info.get('BonusEnhancementType'))
        self.__item_id: int = _parse.pss_int(item_info.get('ItemId'))

    @property
    def item_design_id(self) -> int:
        return self.__item_design_id

    @property
    def bonus_enhancement_value(self) -> float:
        return self.__bonus_enhancement_value

    @property
    def ship_id(self) -> int:
        return self.__ship_id

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def is_new(self) -> bool:
        return self.__is_new

    @property
    def bonus_enhancement_type(self) -> str:
        return self.__bonus_enhancement_type

    @property
    def item_id(self) -> int:
        return self.__item_id
