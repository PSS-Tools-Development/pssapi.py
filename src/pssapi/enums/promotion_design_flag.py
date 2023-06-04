from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class PromotionDesignFlag(_IntFlag):
    NONE = 0
    SHOW_SPLASH = 1
    SHOW_BADGE = 2
    STACKS = 4
    SINGLE_PURCHASE = 8
    SINGLE_PURCHASE_PER_DAY = 16


class PromotionDesignFlagObject(_IntFlagObjectBase):
    def __init__(self, promotion_design_flag: PromotionDesignFlag):
        super().__init__(promotion_design_flag)

    @property
    def show_badge(self) -> bool:
        return bool(self.value & PromotionDesignFlag.SHOW_BADGE)

    @property
    def show_splash(self) -> bool:
        return bool(self.value & PromotionDesignFlag.SHOW_SPLASH)

    @property
    def single_purchase(self) -> bool:
        return bool(self.value & PromotionDesignFlag.SINGLE_PURCHASE)

    @property
    def single_purchase_per_day(self) -> bool:
        return bool(self.value & PromotionDesignFlag.SINGLE_PURCHASE_PER_DAY)

    @property
    def stacks(self) -> bool:
        return bool(self.value & PromotionDesignFlag.STACKS)

    @property
    def value(self) -> PromotionDesignFlag:
        return self._value
