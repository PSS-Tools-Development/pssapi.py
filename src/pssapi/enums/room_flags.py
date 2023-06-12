from enum import IntFlag as _IntFlag


class RoomFlags(_IntFlag):
    NONE = 0
    REQUIRE_POWER = 1
    REQUIRE_TARGET = 2
    REQUIRE_ITEM = 4
    ALLOW_DESIGN_SWITCH = 8
    DISPLAY_WHEN_MISSING_REQUIREMENTS = 16
    DONT_ALLOW_UPGRADE = 32
