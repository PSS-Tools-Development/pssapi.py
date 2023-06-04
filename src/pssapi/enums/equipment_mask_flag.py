from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class EquipmentMaskFlag(_IntFlag):
    NONE = 0
    HEAD = 1
    BODY = 2
    LEG = 4
    WEAPON = 8
    ACCESSORY = 16
    PET = 32


class EquipmentMaskFlagObject(_IntFlagObjectBase):
    def __init__(self, equipment_mask_flag: EquipmentMaskFlag):
        super().__init__(equipment_mask_flag)

    @property
    def accessory(self) -> bool:
        return bool(self.value & EquipmentMaskFlag.ACCESSORY)

    @property
    def body(self) -> bool:
        return bool(self.value & EquipmentMaskFlag.BODY)

    @property
    def head(self) -> bool:
        return bool(self.value & EquipmentMaskFlag.HEAD)

    @property
    def leg(self) -> bool:
        return bool(self.value & EquipmentMaskFlag.LEG)

    @property
    def pet(self) -> bool:
        return bool(self.value & EquipmentMaskFlag.PET)

    @property
    def weapon(self) -> bool:
        return bool(self.value & EquipmentMaskFlag.WEAPON)

    @property
    def value(self) -> EquipmentMaskFlag:
        return self._value
