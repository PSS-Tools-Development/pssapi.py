from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class RoomDesignSpriteFlag(_IntFlag):
    NONE = 0
    HIDE_IF_REQUIREMENT_NOT_MET = 1


class RoomDesignSpriteFlagObject(_IntFlagObjectBase):
    def __init__(self, room_design_sprite_flag: RoomDesignSpriteFlag):
        super().__init__(room_design_sprite_flag)

    @property
    def hide_if_requirement_not_met(self) -> bool:
        return bool(self.value & RoomDesignSpriteFlag.HIDE_IF_REQUIREMENT_NOT_MET)

    @property
    def value(self) -> RoomDesignSpriteFlag:
        return self._value
