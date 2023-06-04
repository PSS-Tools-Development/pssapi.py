from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class MissionDesignFlag(_IntFlag):
    NONE = 0
    HIDE_WHEN_REQUIREMENT_NOT_SATISFIED = 1
    GALAXY_EXCLUSIVE = 2
    SHOWN_WHEN_UNEXPLORED = 4
    DISABLE_HP_CHECK = 8
    VOTES = 16
    IGNORE_STAR_SYSTEM = 32


class MissionDesignFlagObject(_IntFlagObjectBase):
    def __init__(self, mission_design_flag: MissionDesignFlag):
        super().__init__(mission_design_flag)

    @property
    def disable_hp_check(self) -> bool:
        return bool(self.value & MissionDesignFlag.DISABLE_HP_CHECK)

    @property
    def galaxy_exclusive(self) -> bool:
        return bool(self.value & MissionDesignFlag.GALAXY_EXCLUSIVE)

    @property
    def hide_when_requirement_not_satisfied(self) -> bool:
        return bool(self.value & MissionDesignFlag.HIDE_WHEN_REQUIREMENT_NOT_SATISFIED)

    @property
    def ignore_star_system(self) -> bool:
        return bool(self.value & MissionDesignFlag.IGNORE_STAR_SYSTEM)

    @property
    def shown_when_unexplored(self) -> bool:
        return bool(self.value & MissionDesignFlag.SHOWN_WHEN_UNEXPLORED)

    @property
    def votes(self) -> bool:
        return bool(self.value & MissionDesignFlag.VOTES)

    @property
    def value(self) -> MissionDesignFlag:
        return self._value
