from .str_enum_base import StrEnumBase as _StrEnumBase


class ManufactureType(_StrEnumBase):
    NONE = "None"
    ANDROID = "Android"
    CAPACITY = "Capacity"
    CRAFT = "Craft"
    EQUIPMENT = "Equipment"
    GAS = "Gas"
    MINERAL = "Mineral"
    MISSILE = "Missile"
