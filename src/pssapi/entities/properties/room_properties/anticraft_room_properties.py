from .room_properties_base import RoomPropertiesPowerUsedBase


class AntiCraftProperties(RoomPropertiesPowerUsedBase):
    @property
    def max_range(self) -> int:
        """
        The maximum range of the room in pixels.
        """
        return self._room_design.range

    @property
    def min_range(self) -> int:
        """
        The minimum range of the room in pixels.
        """
        return self._room_design.min_range
