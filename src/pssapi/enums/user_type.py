from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class UserType(_StrEnumBase):
    ADMINISTRATOR = "Administrator"
    BACKER = "Backer"
    BANNED = "Banned"
    MISSION = "Mission"
    SYNC_USER = "SyncUser"
    UNVERIFIED = "Unverified"
    ALLIANCE = "UserTypeAlliance"
    COMMUNITY_MANAGER = "UserTypeCommunityManager"
    DESIGNER = "UserTypeDesigner"
    DISABLED = "UserTypeDisabled"
    JAIL_BROKEN = "UserTypeJailBroken"
    LIVE_OPS = "UserTypeLiveOps"
    MODERATOR = "UserTypeModerator"
    PAYING = "UserTypePaying"
    ROBOT = "UserTypeRobot"
    TEMPLATE = "UserTypeTemplate"
    TEST = "UserTypeTest"
    VERIFIED = "Verified"
