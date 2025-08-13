"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class StarSystemRaw(EntityBaseRaw, tag="StarSystem"):
    XML_NODE_NAME: str = "StarSystem"

    exploration_duration: Optional[int] = attr(name="ExplorationDuration", default=None)
    icon_sprite_id: Optional[int] = attr(name="IconSpriteId", default=None)
    requirement_description: Optional[str] = attr(name="RequirementDescription", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    star_system_description: Optional[str] = attr(name="StarSystemDescription", default=None)
    star_system_id: Optional[int] = attr(name="StarSystemId", default=None)
    star_system_title: Optional[str] = attr(name="StarSystemTitle", default=None)
    x: Optional[int] = attr(name="X", default=None)
    y: Optional[int] = attr(name="Y", default=None)
    z: Optional[int] = attr(name="Z", default=None)

    def _key(self):
        return (
            self.exploration_duration,
            self.icon_sprite_id,
            self.requirement_description,
            self.requirement_string,
            self.star_system_description,
            self.star_system_id,
            self.star_system_title,
            self.x,
            self.y,
            self.z,
        )


__all__ = [
    "StarSystemRaw",
]
