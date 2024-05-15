from .... import entities, enums


class RoomPropertiesBase:
    def __init__(self, room_design: "entities.RoomDesign"):
        self._room_design: entities.RoomDesign = room_design

    @property
    def activation_delay(self) -> int:
        return self._room_design.activation_delay

    @property
    def build_time(self) -> int:
        return self._room_design.construction_time

    @property
    def category(self) -> "enums.CategoryType":
        return self._room_design.category_type_enum
    
    @property
    def enhancement_type(self) -> "enums.EnhancementType":
        return self._room_design.enhancement_type_enum

    @property
    def height(self) -> int:
        return self._room_design.rows

    @property
    def innate_armor(self) -> int:
        return self._room_design.default_defence_bonus

    @property
    def level(self) -> int:
        return self._room_design.level

    @property
    def type(self) -> "enums.RoomType":
        return self._room_design.room_type_enum

    @property
    def width(self) -> int:
        return self._room_design.columns


class RoomPropertiesHpBase(RoomPropertiesBase):
    @property
    def max_hp(self) -> int:
        return max(self._room_design.max_power_generated, self._room_design.max_system_power)


class RoomPropertiesPowerGeneratedBase(RoomPropertiesHpBase):
    @property
    def max_power_generated(self) -> int:
        return self._room_design.max_power_generated


class RoomPropertiesPowerUsedBase(RoomPropertiesHpBase):
    @property
    def max_power_used(self) -> int:
        return self._room_design.max_system_power


class RoomPropertiesReloadBase(RoomPropertiesBase):
    @property
    def reload(self) -> float:
        """
        Reload time of the room in seconds.
        """
        return self._room_design.reload_time / 40.0

    @property
    def reloads_per_second(self) -> float:
        """
        Number of reloads per second.
        """
        if self._room_design.reload_time == 0:
            return 0
        return 40.0 / self._room_design.reload_time
