from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


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
        return bool(self.value & ChallengeFlags.IS_FIRST_FREE)

    @property
    def is_manual_command_enabled(self) -> bool:
        return bool(self.value & ChallengeFlags.IS_MANUAL_COMMAND_ENABLED)

    @property
    def is_real_time(self) -> bool:
        return bool(self.value & ChallengeFlags.IS_REAL_TIME)

    @property
    def is_single_play(self) -> bool:
        return bool(self.value & ChallengeFlags.IS_SINGLE_PLAY)

    @property
    def value(self) -> ChallengeFlags:
        return self._value
