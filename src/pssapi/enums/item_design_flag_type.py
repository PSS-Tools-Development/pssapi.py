from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class ItemDesignFlagType(_IntFlag):
    NONE = 0
    ALLOW_TRADING = 1
    DROPSHIP_REWARD = 2
    CHALLENGE_REWARD = 4
    PVP_REWARD = 8
    INSTANT_REWARD = 16
    MISSION_REWARD = 32
    CONSUMABLE = 64
    ALIGN_TO_TOP = 128
    ALLOW_DONATION = 256
    GIFTABLE = 512
    USE_ON_CREW = 1024
    RECYCLING_BUILD = 2048
    USED_ITEM = 4096
    ALLOW_MANUFACTURE = 8192
    TASK_PRIZE = 16384
    UNIQUE_CONTENT_REWARD = 32768
    USE_ON_ROOM = 65536
    DONT_SHOW_REWARDS = 131072


class ItemDesignFlagTypeObject(_IntFlagObjectBase):
    def __init__(self, item_design_flag_type: ItemDesignFlagType):
        super().__init__(item_design_flag_type)

    @property
    def align_to_top(self) -> bool:
        return bool(self.value & ItemDesignFlagType.ALIGN_TO_TOP)

    @property
    def allow_donation(self) -> bool:
        return bool(self.value & ItemDesignFlagType.ALLOW_DONATION)

    @property
    def allow_manufacture(self) -> bool:
        return bool(self.value & ItemDesignFlagType.ALLOW_MANUFACTURE)

    @property
    def allow_trading(self) -> bool:
        return bool(self.value & ItemDesignFlagType.ALLOW_TRADING)

    @property
    def challenge_reward(self) -> bool:
        return bool(self.value & ItemDesignFlagType.CHALLENGE_REWARD)

    @property
    def consumable(self) -> bool:
        return bool(self.value & ItemDesignFlagType.CONSUMABLE)

    @property
    def dont_show_rewards(self) -> bool:
        return bool(self.value & ItemDesignFlagType.DONT_SHOW_REWARDS)

    @property
    def dropship_reward(self) -> bool:
        return bool(self.value & ItemDesignFlagType.DROPSHIP_REWARD)

    @property
    def giftable(self) -> bool:
        return bool(self.value & ItemDesignFlagType.GIFTABLE)

    @property
    def instant_reward(self) -> bool:
        return bool(self.value & ItemDesignFlagType.INSTANT_REWARD)

    @property
    def mission_reward(self) -> bool:
        return bool(self.value & ItemDesignFlagType.MISSION_REWARD)

    @property
    def pvp_reward(self) -> bool:
        return bool(self.value & ItemDesignFlagType.PVP_REWARD)

    @property
    def recycling_build(self) -> bool:
        return bool(self.value & ItemDesignFlagType.RECYCLING_BUILD)

    @property
    def task_prize(self) -> bool:
        return bool(self.value & ItemDesignFlagType.TASK_PRIZE)

    @property
    def unique_content_reward(self) -> bool:
        return bool(self.value & ItemDesignFlagType.UNIQUE_CONTENT_REWARD)

    @property
    def use_on_crew(self) -> bool:
        return bool(self.value & ItemDesignFlagType.USE_ON_CREW)

    @property
    def use_on_room(self) -> bool:
        return bool(self.value & ItemDesignFlagType.USE_ON_ROOM)

    @property
    def used_item(self) -> bool:
        return bool(self.value & ItemDesignFlagType.USED_ITEM)

    @property
    def value(self) -> ItemDesignFlagType:
        return self._value
