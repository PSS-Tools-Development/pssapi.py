from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class FriendType(_StrEnumBase):
    ABUSE = "Abuse"
    APPROVAL = "Approval"
    FACEBOOK_FRIEND = "FacebookFriend"
    FRIEND = "Friend"
    IGNORE = "Ignore"
    INVITED = "Invited"
    UNFRIENDED = "Unfriended"
