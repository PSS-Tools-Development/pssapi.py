from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class SaleItemMask(_IntFlag):
    NONE = 0
    STARBUX_500 = 1
    """Clip of Starbux"""
    STARBUX_1200 = 2
    """Roll of Starbux"""
    STARBUX_2500 = 4
    """Stash of Starbux"""
    STARBUX_6500 = 8
    """Case of Starbux"""
    STARBUX_14000 = 16
    """Vault of Starbux"""
    SALE_1 = 32
    """Promotion.pack_id == 'sale1'"""
    SALE_2 = 64
    """Promotion.pack_id == 'sale2'"""
    SALE_3 = 128
    """Promotion.pack_id == 'sale3'"""
    SALE_4 = 256
    """Promotion.pack_id == 'sale4'"""
    SALE_5 = 512
    """Promotion.pack_id == 'sale5'"""
    SALE_6 = 1024
    """Promotion.pack_id == 'sale6'"""


class SaleItemMaskObject(_IntFlagObjectBase):
    def __init__(self, sale_item_mask: SaleItemMask):
        super().__init__(sale_item_mask)

    @property
    def starbux_500(self) -> bool:
        return bool(self.value & SaleItemMask.STARBUX_500)

    @property
    def starbux_1200(self) -> bool:
        return bool(self.value & SaleItemMask.STARBUX_1200)

    @property
    def starbux_2500(self) -> bool:
        return bool(self.value & SaleItemMask.STARBUX_2500)

    @property
    def starbux_6500(self) -> bool:
        return bool(self.value & SaleItemMask.STARBUX_6500)

    @property
    def starbux_14000(self) -> bool:
        return bool(self.value & SaleItemMask.STARBUX_14000)

    @property
    def sale_1(self) -> bool:
        return bool(self.value & SaleItemMask.SALE_1)

    @property
    def sale_2(self) -> bool:
        return bool(self.value & SaleItemMask.SALE_2)

    @property
    def sale_3(self) -> bool:
        return bool(self.value & SaleItemMask.SALE_3)

    @property
    def sale_4(self) -> bool:
        return bool(self.value & SaleItemMask.SALE_4)

    @property
    def sale_5(self) -> bool:
        return bool(self.value & SaleItemMask.SALE_5)

    @property
    def sale_6(self) -> bool:
        return bool(self.value & SaleItemMask.SALE_6)

    @property
    def value(self) -> SaleItemMask:
        return self._value
