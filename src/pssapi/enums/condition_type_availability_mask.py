from enum import IntFlag as _IntFlag


class ConditionTypeAvailabilityMask(_IntFlag):
    NONE = 0
    TARGET_ROOM = 1
    TARGET_CHARACTER = 2
