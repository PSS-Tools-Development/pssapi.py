from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class EmailVerificationStatus(_StrEnum):
    NONE = "None"
    IS_EMAIL_INVALID = "IsEmailInvalid"
    IS_EMAIL_VALID = "IsEmailValid"
    IS_EMAIL_VERIFIED = "IsEmailVerified"
