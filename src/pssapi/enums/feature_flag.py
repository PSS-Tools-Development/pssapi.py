from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class FeatureFlag(_IntFlag):
    NONE = 0
    GALAXY = 1
    ROOM_REARM = 2
    SHOP_TOPBAR = 4
    APPSFLYER = 8
    BRANCH = 16


class FeatureFlagObject(_IntFlagObjectBase):
    def __init__(self, equipment_mask_flag: FeatureFlag):
        super().__init__(equipment_mask_flag)

    @property
    def appsflyer(self) -> bool:
        return bool(self.value & FeatureFlag.APPSFLYER)

    @property
    def branch(self) -> bool:
        return bool(self.value & FeatureFlag.BRANCH)

    @property
    def galaxy(self) -> bool:
        return bool(self.value & FeatureFlag.GALAXY)

    @property
    def room_rearm(self) -> bool:
        return bool(self.value & FeatureFlag.ROOM_REARM)

    @property
    def shop_topbar(self) -> bool:
        return bool(self.value & FeatureFlag.SHOP_TOPBAR)

    @property
    def value(self) -> FeatureFlag:
        return self._value
