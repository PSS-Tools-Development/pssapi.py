from .str_enum_base import StrEnumBase as _StrEnumBase


class SpriteType(_StrEnumBase):
    NONE = "None"
    INTERIOR = "Interior"
    EXTERIOR = "Exterior"
    INTERIOR_DESTROYED = "InteriorDestroyed"
    EXTERIOR_DESTROYED = "ExteriorDestroyed"
    INTERIOR_ACTIVATE = "InteriorActivate"
    EXTERIOR_ACTIVATE = "ExteriorActivate"
    LOADING = "Loading"
