from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class AssetType(_StrEnumBase):
    NONE = "None"
    SOUND = "Sound"
    SPRITE = "Sprite"
    TEXTURE = "Texture"
    UNITY_MATERIAL = "UnityMaterial"
    UNITY_MODEL = "UnityModel"
