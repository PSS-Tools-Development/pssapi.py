from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class VisibilityFlags(_StrEnumBase):
    NONE = "None"
    HIDE_WHEN_NOT_SATISFIED = "HideWhenNotSatisfied"
    SHOW_WHEN_NOT_SATISFIED = "ShowWhenNotSatisfied"
    ALWAYS_SHOW = "AlwaysShow"
    ALWAYS_HIDE = "AlwaysHide"
