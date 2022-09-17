from enum import IntEnum as _IntEnum

"""
    This file will be generated from decompilation
    and might require manual fixing, if Savy uses
    enum values that are python keywords.
"""


class ItemDesignFlag(_IntEnum):
    AllowTrading = 1
    DropshipReward = 2
    ChallengeReward = 4
    PvpReward = 8
    InstantReward = 16
    MissionReward = 32
    Consumable = 64
    AlignToTop = 128
    AllowDonation = 256
    Giftable = 512
    UseOnCrew = 1024
    RecyclingBuild = 2048
    UsedItem = 4096
    AllowManufacture = 8192
    TaskPrize = 16384
    UniqueContentReward = 32768
    UseOnRoom = 65536
