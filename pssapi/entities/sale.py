from .entity_base import EntityWithIdBase as _EntityWithIdBase
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from datetime import datetime


class Sale(_EntityWithIdBase):
    XML_NODE_NAME: str = 'Sale'

    def __init__(self, _info: _EntityInfo) -> None:
        self.__sale_id: int = _parse.pss_int(_info.get('SaleId'))
        self.__sale_status: str = _parse.pss_str(_info.get('SaleStatus'))
        self.__quantity: int = _parse.pss_int(_info.get('Quantity'))
        self.__currency_type: str = _parse.pss_str(_info.get('CurrencyType'))
        self.__currency_value: int = _parse.pss_int(_info.get('CurrencyValue'))
        self.__seller_ship_id: int = _parse.pss_int(_info.get('SellerShipId'))
        self.__starbux_value: int = _parse.pss_int(_info.get('StarbuxValue'))
        self.__buyer_ship_id: int = _parse.pss_int(_info.get('BuyerShipId'))
        self.__character_id: int = _parse.pss_int(_info.get('CharacterId'))
        self.__status_date: datetime = _parse.pss_datetime(_info.get('StatusDate'))
        self.__item_id: int = _parse.pss_int(_info.get('ItemId'))
        self.__character_design_id: int = _parse.pss_int(_info.get('CharacterDesignId'))
        self.__item_design_id: int = _parse.pss_int(_info.get('ItemDesignId'))
        self.__seller_ship_name: str = _parse.pss_str(_info.get('SellerShipName'))
        self.__buyer_ship_name: str = _parse.pss_str(_info.get('BuyerShipName'))

    def __repr__(self) -> str:
        return f'<Sale {self.id}>'

    def __str__(self) -> str:
        return f'<Sale {self.id}>'

    @property
    def id(self) -> int:
        return self.sale_id

    @property
    def sale_id(self) -> int:
        return self.__sale_id

    @property
    def sale_status(self) -> str:
        return self.__sale_status

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def currency_type(self) -> str:
        return self.__currency_type

    @property
    def currency_value(self) -> int:
        return self.__currency_value

    @property
    def seller_ship_id(self) -> int:
        return self.__seller_ship_id

    @property
    def starbux_value(self) -> int:
        return self.__starbux_value

    @property
    def buyer_ship_id(self) -> int:
        return self.__buyer_ship_id

    @property
    def character_id(self) -> int:
        return self.__character_id

    @property
    def status_date(self) -> datetime:
        return self.__status_date

    @property
    def item_id(self) -> int:
        return self.__item_id

    @property
    def character_design_id(self) -> int:
        return self.__character_design_id

    @property
    def item_design_id(self) -> int:
        return self.__item_design_id

    @property
    def seller_ship_name(self) -> str:
        return self.__seller_ship_name

    @property
    def buyer_ship_name(self) -> str:
        return self.__buyer_ship_name
