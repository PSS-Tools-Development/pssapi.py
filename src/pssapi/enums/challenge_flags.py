from enum import IntFlag as _IntFlag

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


class ChallengeFlagsObject(object):
    def __init__(self, challenge_flags: ChallengeFlags):
        self._is_real_time: bool = False
        self._is_first_free: bool = False
        self._is_single_play: bool = False
        self._is_manual_command_enabled: bool = False
        if challenge_flags:
            self._is_real_time = challenge_flags & ChallengeFlags.IS_REAL_TIME or False
            self._is_first_free = challenge_flags & ChallengeFlags.IS_FIRST_FREE or False
            self._is_single_play = challenge_flags & ChallengeFlags.IS_SINGLE_PLAY or False
            self._is_manual_command_enabled = challenge_flags & ChallengeFlags.IS_MANUAL_COMMAND_ENABLED or False

    @property
    def is_real_time(self) -> bool:
        return self._is_real_time

    @property
    def is_first_free(self) -> bool:
        return self._is_first_free

    @property
    def is_single_play(self) -> bool:
        return self._is_single_play

    @property
    def is_manual_command_enabled(self) -> bool:
        return self._is_manual_command_enabled
