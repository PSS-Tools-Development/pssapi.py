from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class TaskDesignFlagsType(_IntFlag):
    NONE = 1


class TaskDesignFlagsTypeObject(_IntFlagObjectBase):
    def __init__(self, task_design_flags_type: TaskDesignFlagsType):
        super().__init__(task_design_flags_type)

    @property
    def value(self) -> TaskDesignFlagsType:
        return self._value
