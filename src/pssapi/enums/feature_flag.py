from enum import IntFlag as _IntFlag


class FeatureFlag(_IntFlag):
    NONE = 0
    GALAXY = 1
    ROOM_REARM = 2
    SHOP_TOPBAR = 4
    APPSFLYER = 8
    BRANCH = 16
