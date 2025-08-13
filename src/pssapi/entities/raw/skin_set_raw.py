"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class SkinSetRaw(EntityBaseRaw, tag="SkinSet"):
    XML_NODE_NAME: str = "SkinSet"

    approval_flags: Optional[str] = attr(name="ApprovalFlags", default=None)
    cost_string: Optional[str] = attr(name="CostString", default=None)
    date_updated: Optional[datetime] = attr(name="DateUpdated", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    skin_set_description: Optional[str] = attr(name="SkinSetDescription", default=None)
    skin_set_id: Optional[int] = attr(name="SkinSetId", default=None)
    skin_set_name: Optional[str] = attr(name="SkinSetName", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)

    def _key(self):
        return (
            self.approval_flags,
            self.cost_string,
            self.date_updated,
            self.flags,
            self.metadata,
            self.requirement_string,
            self.skin_set_description,
            self.skin_set_id,
            self.skin_set_name,
            self.sprite_id,
        )


__all__ = [
    "SkinSetRaw",
]
