from enum import IntFlag as _IntFlag


class AvailabilityMask(_IntFlag):
    NONE = 0
    PLAYER = 1
    """Available on a player's ship."""
    ALLIANCE = 2
    """Available on a fleet's starbase."""


class AvailabilityMaskObject(object):
    def __init__(self, availability_mask: AvailabilityMask):
        self._player: bool = False
        self._alliance: bool = False
        if availability_mask:
            self._player: bool = availability_mask & AvailabilityMask.PLAYER or False
            self._alliance: bool = availability_mask & AvailabilityMask.PLAYER or False

    @property
    def player(self) -> bool:
        return self._player

    @property
    def alliance(self) -> bool:
        return self._alliance
