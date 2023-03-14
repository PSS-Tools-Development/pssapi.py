from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ActivityType(_StrEnum):
    REPLAY = "Replay"
    APPLICATION = "Application"
    JOINED = "Joined"
    MEMBERSHIP_CHANGED = "MembershipChanged"
    INVITED = "Invited"
    DONATED = "Donated"
    REWARD = "Reward"
    REWARD_COLLECTED = "RewardCollected"
    DEVICE_LOGIN = "DeviceLogin"
    MARKET_LISTED = "MarketListed"
    MARKET_SOLD = "MarketSold"
    MARKET_EXPIRED = "MarketExpired"
    REWARD_PENDING = "RewardPending"
    UNFRIENDED = "Unfriended"
    BATTLE_MATCHED = "BattleMatched"
    BATTLE_LOAD_PROGRESS = "BattleLoadProgress"
    ALLIANCE_SETTINGS_UPDATED = "AllianceSettingsUpdated"
    ALLIANCE_QUALIFIED = "AllianceQualified"
    ACTIONED = "Actioned"
    MODEL_UPDATE = "ModelUpdate"
    FRIEND_REQUEST_DECLINE = "FriendRequestDecline"
    FRIEND_REQUEST_ACCEPT = "FriendRequestAccept"
    ALLIANCE_ANNOUNCEMENT = "AllianceAnnouncement"
    RELOAD_USER_DATA = "ReloadUserData"
    FRIEND_REQUEST_CANCEL = "FriendRequestCancel"
    GIFT = "Gift"
