from enum import IntFlag as _IntFlag


class AvailabilityMask(_IntFlag):
    PLAYER = 1
    """Available on a player's ship."""
    ALLIANCE = 2
    """Available on a fleet's starbase."""
