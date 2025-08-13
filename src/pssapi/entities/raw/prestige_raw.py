"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class PrestigeRaw(EntityBaseRaw, tag="Prestige"):
    XML_NODE_NAME: str = "Prestige"

    character_design_id_1: Optional[int] = attr(name="CharacterDesignId1", default=None)
    character_design_id_2: Optional[int] = attr(name="CharacterDesignId2", default=None)
    to_character_design_id: Optional[int] = attr(name="ToCharacterDesignId", default=None)

    def _key(self):
        return (
            self.character_design_id_1,
            self.character_design_id_2,
            self.to_character_design_id,
        )


__all__ = [
    "PrestigeRaw",
]
