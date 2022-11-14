"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class SaleRaw:
    XML_NODE_NAME: str = 'Sale'

    def __init__(self, sale_info: _EntityInfo) -> None:
        self.buyer_ship_id: int = _parse.pss_int(sale_info.get('BuyerShipId'))
        self.buyer_ship_name: str = _parse.pss_str(sale_info.get('BuyerShipName'))
        self.character_design_id: int = _parse.pss_int(sale_info.get('CharacterDesignId'))
        self.character_id: int = _parse.pss_int(sale_info.get('CharacterId'))
        self.currency_type: str = _parse.pss_str(sale_info.get('CurrencyType'))
        self.currency_value: int = _parse.pss_int(sale_info.get('CurrencyValue'))
        self.item_design_id: int = _parse.pss_int(sale_info.get('ItemDesignId'))
        self.item_id: int = _parse.pss_int(sale_info.get('ItemId'))
        self.quantity: int = _parse.pss_int(sale_info.get('Quantity'))
        self.sale_id: int = _parse.pss_int(sale_info.get('SaleId'))
        self.sale_status: str = _parse.pss_str(sale_info.get('SaleStatus'))
        self.seller_ship_id: int = _parse.pss_int(sale_info.get('SellerShipId'))
        self.seller_ship_name: str = _parse.pss_str(sale_info.get('SellerShipName'))
        self.starbux_value: int = _parse.pss_int(sale_info.get('StarbuxValue'))
        self.status_date: _datetime = _parse.pss_datetime(sale_info.get('StatusDate'))
