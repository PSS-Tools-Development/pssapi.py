from enum import IntFlag as _IntFlag

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ItemDesignFlagType(_IntFlag):
    NONE = 0
    ALLOW_TRADING = 1
    DROPSHIP_REWARD = 2
    CHALLENGE_REWARD = 4
    PVP_REWARD = 8
    INSTANT_REWARD = 16
    MISSION_REWARD = 32
    CONSUMABLE = 64
    ALIGN_TO_TOP = 128
    ALLOW_DONATION = 256
    GIFTABLE = 512
    USE_ON_CREW = 1024
    RECYCLING_BUILD = 2048
    USED_ITEM = 4096
    ALLOW_MANUFACTURE = 8192
    TASK_PRIZE = 16384
    UNIQUE_CONTENT_REWARD = 32768
    USE_ON_ROOM = 65536
    DONT_SHOW_REWARDS = 131072
