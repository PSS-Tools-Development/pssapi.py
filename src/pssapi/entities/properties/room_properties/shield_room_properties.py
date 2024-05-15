from .room_properties_base import RoomPropertiesHpBase


class ShieldRoomProperties(RoomPropertiesHpBase):
    @property
    def shield_hp(self) -> int:
        """
        Amount of shield HP added to maximum shield HP.
        """
        return self._room_design.capacity

    @property
    def restore_on_reload(self) -> float:
        """
        Amount of shield HP added, when the room reloads.
        """
        return self._room_design.manufacture_capacity / 100.0
