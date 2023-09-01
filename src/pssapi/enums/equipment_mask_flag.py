from enum import IntFlag as _IntFlag


class EquipmentMaskFlag(_IntFlag):
    NONE = 0
    HEAD = 1
    BODY = 2
    LEG = 4
    WEAPON = 8
    ACCESSORY = 16
    PET = 32
