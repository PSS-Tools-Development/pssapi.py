from .room_properties_base import RoomPropertiesPowerUsedBase


class RecyclingRoomProperties(RoomPropertiesPowerUsedBase):
    @property
    def gas_per_crew(self) -> int:
        """
        Gas collected per crew that died in battle.
        """
        return self._room_design.manufacture_rate

    @property
    def max_crew_blend(self) -> int:
        """
        Maximum number of crews the player can blend, before an item has to be crafted.
        """
        return self._room_design.manufacture_capacity

    @property
    def max_storage(self) -> int:
        """
        The maximum DNA that can be stored.
        """
        return self._room_design.capacity
