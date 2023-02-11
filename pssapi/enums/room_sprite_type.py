from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""

class RoomSpriteType(_StrEnum):
        INTERIOR = 'Interior'
        EXTERIOR = 'Exterior'
        INTERIOR_DESTROYED = 'InteriorDestroyed'
        EXTERIOR_DESTROYED = 'ExteriorDestroyed'
        INTERIOR_ACTIVATE = 'InteriorActivate'
        EXTERIOR_ACTIVATE = 'ExteriorActivate'
        LOADING = 'Loading'
    