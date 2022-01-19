from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ActivityType(_StrEnum):
    NONE = "None"
    ACTIONED = "Actioned"
    ALLIANCE_ANNOUNCEMENT = "AllianceAnnouncement"
    ALLIANCE_QUALIFIED = "AllianceQualified"
    ALLIANCE_SETTINGS_UPDATED = "AllianceSettingsUpdated"
    APPLICATION = "Application"
    BATTLE_LOAD_PROGRESS = "BattleLoadProgress"
    BATTLE_MATCHED = "BattleMatched"
    DEVICE_LOGIN = "DeviceLogin"
    DONATED = "Donated"
    FRIEND_REQUEST_ACCEPT = "FriendRequestAccept"
    FRIEND_REQUEST_CANCEL = "FriendRequestCancel"
    FRIEND_REQUEST_DECLINE = "FriendRequestDecline"
    GIFT = "Gift"
    INVITED = "Invited"
    JOINED = "Joined"
    MARKET_EXPIRED = "MarketExpired"
    MARKET_LISTED = "MarketListed"
    MARKET_SOLD = "MarketSold"
    MEMBERSHIP_CHANGED = "MembershipChanged"
    MODEL_UPDATE = "ModelUpdate"
    RELOAD_USER_DATA = "ReloadUserData"
    REPLAY = "Replay"
    REWARD = "Reward"
    REWARD_COLLECTED = "RewardCollected"
    REWARD_PENDING = "RewardPending"
    UNFRIENDED = "Unfriended"
