from enum import IntFlag as _IntFlag


class IntFlagObjectBase(object):
    def __init__(self, int_flag: _IntFlag):
        self._value: _IntFlag = int_flag or 0

    @property
    def value(self) -> _IntFlag:
        return self._value
