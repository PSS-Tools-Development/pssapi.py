"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class RoomActionRaw(EntityBaseRaw, tag="RoomAction"):
    XML_NODE_NAME: str = "RoomAction"

    action_type_id: Optional[int] = attr(name="ActionTypeId", default=None)
    condition_type_id: Optional[int] = attr(name="ConditionTypeId", default=None)
    room_action_id: Optional[int] = attr(name="RoomActionId", default=None)
    room_action_index: Optional[int] = attr(name="RoomActionIndex", default=None)
    room_id: Optional[int] = attr(name="RoomId", default=None)

    def _key(self):
        return (
            self.action_type_id,
            self.condition_type_id,
            self.room_action_id,
            self.room_action_index,
            self.room_id,
        )


__all__ = [
    "RoomActionRaw",
]
