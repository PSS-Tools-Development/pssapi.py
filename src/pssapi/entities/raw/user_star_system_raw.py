"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class UserStarSystemRaw(EntityBaseRaw, tag="UserStarSystem"):
    XML_NODE_NAME: str = "UserStarSystem"

    exploration_percentage: Optional[int] = attr(name="ExplorationPercentage", default=None)
    star_system_id: Optional[int] = attr(name="StarSystemId", default=None)
    user_id: Optional[int] = attr(name="UserId", default=None)
    user_star_system_id: Optional[int] = attr(name="UserStarSystemId", default=None)

    def _key(self):
        return (
            self.exploration_percentage,
            self.star_system_id,
            self.user_id,
            self.user_star_system_id,
        )


__all__ = [
    "UserStarSystemRaw",
]
