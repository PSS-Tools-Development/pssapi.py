from enum import IntFlag as _IntFlag


class SaleItemMask(_IntFlag):
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
