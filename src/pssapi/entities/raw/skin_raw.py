"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class SkinRaw(EntityBaseRaw, tag="Skin"):
    XML_NODE_NAME: str = "Skin"

    animation_id: Optional[int] = attr(name="AnimationId", default=None)
    approval_flags: Optional[str] = attr(name="ApprovalFlags", default=None)
    date_updated: Optional[datetime] = attr(name="DateUpdated", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    original_animation_id: Optional[int] = attr(name="OriginalAnimationId", default=None)
    original_sprite_id: Optional[int] = attr(name="OriginalSpriteId", default=None)
    race_id: Optional[int] = attr(name="RaceId", default=None)
    reference_id: Optional[int] = attr(name="ReferenceId", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    root_id: Optional[int] = attr(name="RootId", default=None)
    skin_description: Optional[str] = attr(name="SkinDescription", default=None)
    skin_id: Optional[int] = attr(name="SkinId", default=None)
    skin_name: Optional[str] = attr(name="SkinName", default=None)
    skin_set_id: Optional[int] = attr(name="SkinSetId", default=None)
    skin_type: Optional[str] = attr(name="SkinType", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)
    sprite_type: Optional[str] = attr(name="SpriteType", default=None)
    user_id: Optional[int] = attr(name="UserId", default=None)

    def _key(self):
        return (
            self.animation_id,
            self.approval_flags,
            self.date_updated,
            self.flags,
            self.metadata,
            self.original_animation_id,
            self.original_sprite_id,
            self.race_id,
            self.reference_id,
            self.requirement_string,
            self.root_id,
            self.skin_description,
            self.skin_id,
            self.skin_name,
            self.skin_set_id,
            self.skin_type,
            self.sprite_id,
            self.sprite_type,
            self.user_id,
        )


__all__ = [
    "SkinRaw",
]
