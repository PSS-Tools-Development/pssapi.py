from enum import IntFlag as _IntFlag

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class PromotionDesignFlag(_IntFlag):
    NONE = 0
    SHOW_SPLASH = 1
    SHOW_BADGE = 2
    STACKS = 4
    SINGLE_PURCHASE = 8
    SINGLE_PURCHASE_PER_DAY = 16
