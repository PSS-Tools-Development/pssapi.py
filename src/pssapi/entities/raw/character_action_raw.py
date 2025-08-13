"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class CharacterActionRaw(EntityBaseRaw, tag="CharacterAction"):
    XML_NODE_NAME: str = "CharacterAction"

    action_type_id: Optional[int] = attr(name="ActionTypeId", default=None)
    character_action_id: Optional[int] = attr(name="CharacterActionId", default=None)
    character_action_index: Optional[int] = attr(name="CharacterActionIndex", default=None)
    character_id: Optional[int] = attr(name="CharacterId", default=None)
    condition_type_id: Optional[int] = attr(name="ConditionTypeId", default=None)

    def _key(self):
        return (
            self.action_type_id,
            self.character_action_id,
            self.character_action_index,
            self.character_id,
            self.condition_type_id,
        )


__all__ = [
    "CharacterActionRaw",
]
