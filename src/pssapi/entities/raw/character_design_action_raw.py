"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class CharacterDesignActionRaw(EntityBaseRaw, tag="CharacterDesignAction"):
    XML_NODE_NAME: str = "CharacterDesignAction"

    action_type_id: Optional[int] = attr(name="ActionTypeId", default=None)
    character_design_action_id: Optional[int] = attr(name="CharacterDesignActionId", default=None)
    character_design_action_index: Optional[int] = attr(name="CharacterDesignActionIndex", default=None)
    character_design_id: Optional[int] = attr(name="CharacterDesignId", default=None)
    condition_type_id: Optional[int] = attr(name="ConditionTypeId", default=None)

    def _key(self):
        return (
            self.action_type_id,
            self.character_design_action_id,
            self.character_design_action_index,
            self.character_design_id,
            self.condition_type_id,
        )


__all__ = [
    "CharacterDesignActionRaw",
]
