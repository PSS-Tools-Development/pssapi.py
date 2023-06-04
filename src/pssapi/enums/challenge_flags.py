from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ChallengeFlags(_IntFlag):
    NONE = 0
    IS_REAL_TIME = 1
    IS_FIRST_FREE = 2
    IS_SINGLE_PLAY = 4
    IS_MANUAL_COMMAND_ENABLED = 8


class ChallengeFlagsObject(_IntFlagObjectBase):
    def __init__(self, challenge_flags: ChallengeFlags):
        super().__init__(challenge_flags)

    @property
    def is_first_free(self) -> bool:
        return self.value & ChallengeFlags.IS_FIRST_FREE or False

    @property
    def is_manual_command_enabled(self) -> bool:
        return self.value & ChallengeFlags.IS_MANUAL_COMMAND_ENABLED or False

    @property
    def is_real_time(self) -> bool:
        return self.value & ChallengeFlags.IS_REAL_TIME or False

    @property
    def is_single_play(self) -> bool:
        return self.value & ChallengeFlags.IS_SINGLE_PLAY or False

    @property
    def value(self) -> ChallengeFlags:
        return self._value
