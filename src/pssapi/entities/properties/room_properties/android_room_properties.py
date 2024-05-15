from .room_properties_base import RoomPropertiesPowerUsedBase


class AndroidRoomProperties(RoomPropertiesPowerUsedBase):
    @property
    def deploy_limit(self) -> int:
        """
        The maximum number of droids the room can have deployed at the same time.
        """
        return self._room_design.range

    @property
    def queue_limit(self) -> int:
        """
        The limit of the build queue.
        """
        return self._room_design.manufacture_capacity

    @property
    def storage_limit(self) -> int:
        """
        The maximum number of droids the room can store.
        """
        return self._room_design.capacity
