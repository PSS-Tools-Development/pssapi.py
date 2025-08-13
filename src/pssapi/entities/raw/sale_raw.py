"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class SaleRaw(EntityBaseRaw, tag="Sale"):
    XML_NODE_NAME: str = "Sale"

    buyer_ship_id: Optional[int] = attr(name="BuyerShipId", default=None)
    buyer_ship_name: Optional[str] = attr(name="BuyerShipName", default=None)
    character_design_id: Optional[int] = attr(name="CharacterDesignId", default=None)
    character_id: Optional[int] = attr(name="CharacterId", default=None)
    currency_type: Optional[str] = attr(name="CurrencyType", default=None)
    currency_value: Optional[int] = attr(name="CurrencyValue", default=None)
    item_design_id: Optional[int] = attr(name="ItemDesignId", default=None)
    item_id: Optional[int] = attr(name="ItemId", default=None)
    quantity: Optional[int] = attr(name="Quantity", default=None)
    sale_id: Optional[int] = attr(name="SaleId", default=None)
    sale_status: Optional[str] = attr(name="SaleStatus", default=None)
    seller_ship_id: Optional[int] = attr(name="SellerShipId", default=None)
    seller_ship_name: Optional[str] = attr(name="SellerShipName", default=None)
    starbux_value: Optional[int] = attr(name="StarbuxValue", default=None)
    status_date: Optional[datetime] = attr(name="StatusDate", default=None)

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


__all__ = [
    "SaleRaw",
]
