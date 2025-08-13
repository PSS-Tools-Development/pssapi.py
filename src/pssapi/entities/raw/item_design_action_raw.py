"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class ItemDesignActionRaw(EntityBaseRaw, tag="ItemDesignAction"):
    XML_NODE_NAME: str = "ItemDesignAction"

    action_type_id: Optional[int] = attr(name="ActionTypeId", default=None)
    condition_type_id: Optional[int] = attr(name="ConditionTypeId", default=None)
    item_design_action_id: Optional[int] = attr(name="ItemDesignActionId", default=None)
    item_design_action_index: Optional[int] = attr(name="ItemDesignActionIndex", default=None)
    item_design_id: Optional[int] = attr(name="ItemDesignId", default=None)

    def _key(self):
        return (
            self.action_type_id,
            self.condition_type_id,
            self.item_design_action_id,
            self.item_design_action_index,
            self.item_design_id,
        )


__all__ = [
    "ItemDesignActionRaw",
]
