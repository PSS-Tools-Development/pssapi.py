from .str_enum_base import StrEnumBase as _StrEnumBase


"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class AuthenticationType(_StrEnumBase):
    NONE = "None"
    BASIC = "Basic"
    JWT = "JWT"
    SMS = "SMS"
