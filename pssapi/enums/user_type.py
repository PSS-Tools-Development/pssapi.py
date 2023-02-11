from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""

class UserType(_StrEnum):
        UNVERIFIED = 'Unverified'
        VERIFIED = 'Verified'
        ADMINISTRATOR = 'Administrator'
        BANNED = 'Banned'
        BACKER = 'Backer'
        MISSION = 'Mission'
        USER_TYPE_PAYING = 'UserTypePaying'
        USER_TYPE_JAIL_BROKEN = 'UserTypeJailBroken'
        USER_TYPE_ALLIANCE = 'UserTypeAlliance'
        USER_TYPE_MODERATOR = 'UserTypeModerator'
        USER_TYPE_TEMPLATE = 'UserTypeTemplate'
        USER_TYPE_COMMUNITY_MANAGER = 'UserTypeCommunityManager'
        SYNC_USER = 'SyncUser'
        USER_TYPE_DESIGNER = 'UserTypeDesigner'
        USER_TYPE_LIVE_OPS = 'UserTypeLiveOps'
        USER_TYPE_TEST = 'UserTypeTest'
        USER_TYPE_DISABLED = 'UserTypeDisabled'
    