from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class RoomSpriteType(_StrEnumBase):
    EXTERIOR = "Exterior"
    EXTERIOR_ACTIVATE = "ExteriorActivate"
    EXTERIOR_DESTROYED = "ExteriorDestroyed"
    INTERIOR = "Interior"
    INTERIOR_ACTIVATE = "InteriorActivate"
    INTERIOR_DESTROYED = "InteriorDestroyed"
    LOADING = "Loading"
