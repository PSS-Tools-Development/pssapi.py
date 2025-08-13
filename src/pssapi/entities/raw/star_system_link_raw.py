"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class StarSystemLinkRaw(EntityBaseRaw, tag="StarSystemLink"):
    XML_NODE_NAME: str = "StarSystemLink"

    from_star_system_id: Optional[int] = attr(name="FromStarSystemId", default=None)
    is_two_way: Optional[bool] = attr(name="IsTwoWay", default=None)
    star_system_link_id: Optional[int] = attr(name="StarSystemLinkId", default=None)
    to_star_system_id: Optional[int] = attr(name="ToStarSystemId", default=None)
    travel_time: Optional[int] = attr(name="TravelTime", default=None)

    def _key(self):
        return (
            self.from_star_system_id,
            self.is_two_way,
            self.star_system_link_id,
            self.to_star_system_id,
            self.travel_time,
        )


__all__ = [
    "StarSystemLinkRaw",
]
