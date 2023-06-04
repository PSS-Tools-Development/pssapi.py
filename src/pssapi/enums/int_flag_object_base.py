from enum import IntFlag as _IntFlag


class IntFlagObjectBase(object):
    def __init__(self, int_flag: _IntFlag):
        self._value: _IntFlag = int_flag or 0

    @property
    def value(self) -> _IntFlag:
        """Override this property in inheriting classes with the correct data type for code completion to work."""
        return self._value
