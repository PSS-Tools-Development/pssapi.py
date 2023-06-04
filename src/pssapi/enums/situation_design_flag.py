from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class SituationDesignFlag(_IntFlag):
    NONE = 0
    AFFECT_ATTACKING_SHIP = 1
    AFFECT_DEFENDING_SHIP = 2
    AFFECT_PVP = 4
    AFFECT_PVE = 8
    VOTES = 16
    AFFECT_TOURNAMENT = 32


class SituationDesignFlagObject(_IntFlagObjectBase):
    def __init__(self, situation_design_flag: SituationDesignFlag):
        super().__init__(situation_design_flag)

    @property
    def affect_attacking_ship(self) -> bool:
        return bool(self.value & SituationDesignFlag.AFFECT_ATTACKING_SHIP)

    @property
    def affect_defending_ship(self) -> bool:
        return bool(self.value & SituationDesignFlag.AFFECT_DEFENDING_SHIP)

    @property
    def affect_pve(self) -> bool:
        return bool(self.value & SituationDesignFlag.AFFECT_PVE)

    @property
    def affect_pvp(self) -> bool:
        return bool(self.value & SituationDesignFlag.AFFECT_PVP)

    @property
    def affect_tournament(self) -> bool:
        return bool(self.value & SituationDesignFlag.AFFECT_TOURNAMENT)

    @property
    def votes(self) -> bool:
        return bool(self.value & SituationDesignFlag.VOTES)

    @property
    def value(self) -> SituationDesignFlag:
        return self._value
