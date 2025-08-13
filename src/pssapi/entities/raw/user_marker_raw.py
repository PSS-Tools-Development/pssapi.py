"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class UserMarkerRaw(EntityBaseRaw, tag="UserMarker"):
    XML_NODE_NAME: str = "UserMarker"

    is_collected: Optional[bool] = attr(name="IsCollected", default=None)
    last_update_date: Optional[datetime] = attr(name="LastUpdateDate", default=None)
    marker_progress_value: Optional[int] = attr(name="MarkerProgressValue", default=None)
    purchase_flags: Optional[int] = attr(name="PurchaseFlags", default=None)
    star_system_marker_id: Optional[int] = attr(name="StarSystemMarkerId", default=None)
    user_id: Optional[int] = attr(name="UserId", default=None)
    user_marker_id: Optional[int] = attr(name="UserMarkerId", default=None)

    def _key(self):
        return (
            self.is_collected,
            self.last_update_date,
            self.marker_progress_value,
            self.purchase_flags,
            self.star_system_marker_id,
            self.user_id,
            self.user_marker_id,
        )


__all__ = [
    "UserMarkerRaw",
]
