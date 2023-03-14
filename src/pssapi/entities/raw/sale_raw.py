"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class SaleRaw:
    XML_NODE_NAME: str = "Sale"

    def __init__(self, sale_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._buyer_ship_id: int = _parse.pss_int(sale_info.get("BuyerShipId"))
        self._buyer_ship_name: str = _parse.pss_str(sale_info.get("BuyerShipName"))
        self._character_design_id: int = _parse.pss_int(sale_info.get("CharacterDesignId"))
        self._character_id: int = _parse.pss_int(sale_info.get("CharacterId"))
        self._currency_type: str = _parse.pss_str(sale_info.get("CurrencyType"))
        self._currency_value: int = _parse.pss_int(sale_info.get("CurrencyValue"))
        self._item_design_id: int = _parse.pss_int(sale_info.get("ItemDesignId"))
        self._item_id: int = _parse.pss_int(sale_info.get("ItemId"))
        self._quantity: int = _parse.pss_int(sale_info.get("Quantity"))
        self._sale_id: int = _parse.pss_int(sale_info.get("SaleId"))
        self._sale_status: str = _parse.pss_str(sale_info.get("SaleStatus"))
        self._seller_ship_id: int = _parse.pss_int(sale_info.get("SellerShipId"))
        self._seller_ship_name: str = _parse.pss_str(sale_info.get("SellerShipName"))
        self._starbux_value: int = _parse.pss_int(sale_info.get("StarbuxValue"))
        self._status_date: _datetime = _parse.pss_datetime(sale_info.get("StatusDate"))

    @property
    def buyer_ship_id(self) -> int:
        return self._buyer_ship_id

    @property
    def buyer_ship_name(self) -> str:
        return self._buyer_ship_name

    @property
    def character_design_id(self) -> int:
        return self._character_design_id

    @property
    def character_id(self) -> int:
        return self._character_id

    @property
    def currency_type(self) -> str:
        return self._currency_type

    @property
    def currency_value(self) -> int:
        return self._currency_value

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
    def sale_id(self) -> int:
        return self._sale_id

    @property
    def sale_status(self) -> str:
        return self._sale_status

    @property
    def seller_ship_id(self) -> int:
        return self._seller_ship_id

    @property
    def seller_ship_name(self) -> str:
        return self._seller_ship_name

    @property
    def starbux_value(self) -> int:
        return self._starbux_value

    @property
    def status_date(self) -> _datetime:
        return self._status_date

    def _key(self):
        return (
            self.buyer_ship_id,
            self.buyer_ship_name,
            self.character_design_id,
            self.character_id,
            self.currency_type,
            self.currency_value,
            self.item_design_id,
            self.item_id,
            self.quantity,
            self.sale_id,
            self.sale_status,
            self.seller_ship_id,
            self.seller_ship_name,
            self.starbux_value,
            self.status_date,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BuyerShipId": self.buyer_ship_id,
                "BuyerShipName": self.buyer_ship_name,
                "CharacterDesignId": self.character_design_id,
                "CharacterId": self.character_id,
                "CurrencyType": self.currency_type,
                "CurrencyValue": self.currency_value,
                "ItemDesignId": self.item_design_id,
                "ItemId": self.item_id,
                "Quantity": self.quantity,
                "SaleId": self.sale_id,
                "SaleStatus": self.sale_status,
                "SellerShipId": self.seller_ship_id,
                "SellerShipName": self.seller_ship_name,
                "StarbuxValue": self.starbux_value,
                "StatusDate": self.status_date,
            }

        return self._dict
