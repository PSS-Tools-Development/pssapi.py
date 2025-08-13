"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class CharacterPartRaw(EntityBaseRaw, tag="CharacterPart"):
    XML_NODE_NAME: str = "CharacterPart"

    action_border_file_id: Optional[int] = attr(name="ActionBorderFileId", default=None)
    action_file_id: Optional[int] = attr(name="ActionFileId", default=None)
    action_sprite_id: Optional[int] = attr(name="ActionSpriteId", default=None)
    character_part_id: Optional[int] = attr(name="CharacterPartId", default=None)
    character_part_name: Optional[str] = attr(name="CharacterPartName", default=None)
    character_part_type: Optional[str] = attr(name="CharacterPartType", default=None)
    standard_border_file_id: Optional[int] = attr(name="StandardBorderFileId", default=None)
    standard_file_id: Optional[int] = attr(name="StandardFileId", default=None)
    standard_sprite_id: Optional[int] = attr(name="StandardSpriteId", default=None)

    def _key(self):
        return (
            self.action_border_file_id,
            self.action_file_id,
            self.action_sprite_id,
            self.character_part_id,
            self.character_part_name,
            self.character_part_type,
            self.standard_border_file_id,
            self.standard_file_id,
            self.standard_sprite_id,
        )


__all__ = [
    "CharacterPartRaw",
]
