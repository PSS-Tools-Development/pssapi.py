"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ItemRaw:
    XML_NODE_NAME: str = 'Item'

    def __init__(self, item_info: _EntityInfo) -> None:
        self.bonus_enhancement_type: str = _parse.pss_str(
            item_info.get('BonusEnhancementType'))
        self.bonus_enhancement_value: float = _parse.pss_float(
            item_info.get('BonusEnhancementValue'))
        self.is_new: bool = _parse.pss_bool(item_info.get('IsNew'))
        self.item_design_id: int = _parse.pss_int(
            item_info.get('ItemDesignId'))
        self.item_id: int = _parse.pss_int(item_info.get('ItemId'))
        self.quantity: int = _parse.pss_int(item_info.get('Quantity'))
        self.ship_id: int = _parse.pss_int(item_info.get('ShipId'))
