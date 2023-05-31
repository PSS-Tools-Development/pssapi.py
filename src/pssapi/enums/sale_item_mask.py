from enum import IntFlag as _IntFlag


class SaleItemMask(_IntFlag):
    CLIP = 1
    ROLL = 2
    STASH = 4
    CASE = 8
    VAULT = 16
