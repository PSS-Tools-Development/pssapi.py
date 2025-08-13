"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class ActionTypeRaw(EntityBaseRaw, tag="ActionType"):
    XML_NODE_NAME: str = "ActionType"

    action_type_category: Optional[str] = attr(name="ActionTypeCategory", default=None)
    action_type_description: Optional[str] = attr(name="ActionTypeDescription", default=None)
    action_type_id: Optional[int] = attr(name="ActionTypeId", default=None)
    action_type_key: Optional[str] = attr(name="ActionTypeKey", default=None)
    action_type_name: Optional[str] = attr(name="ActionTypeName", default=None)
    action_type_parameter_relativity: Optional[str] = attr(name="ActionTypeParameterRelativity", default=None)
    action_type_parameter_value: Optional[int] = attr(name="ActionTypeParameterValue", default=None)
    color_string: Optional[str] = attr(name="ColorString", default=None)
    condition_parameter_argument: Optional[int] = attr(name="ConditionParameterArgument", default=None)
    condition_type_category: Optional[str] = attr(name="ConditionTypeCategory", default=None)
    condition_type_parameter: Optional[str] = attr(name="ConditionTypeParameter", default=None)
    image_sprite_id: Optional[int] = attr(name="ImageSpriteId", default=None)
    order_index: Optional[int] = attr(name="OrderIndex", default=None)
    required_research_design_id: Optional[int] = attr(name="RequiredResearchDesignId", default=None)
    room_category_type: Optional[str] = attr(name="RoomCategoryType", default=None)
    room_type: Optional[str] = attr(name="RoomType", default=None)

    def _key(self):
        return (
            self.action_type_category,
            self.action_type_description,
            self.action_type_id,
            self.action_type_key,
            self.action_type_name,
            self.action_type_parameter_relativity,
            self.action_type_parameter_value,
            self.color_string,
            self.condition_parameter_argument,
            self.condition_type_category,
            self.condition_type_parameter,
            self.image_sprite_id,
            self.order_index,
            self.required_research_design_id,
            self.room_category_type,
            self.room_type,
        )


__all__ = [
    "ActionTypeRaw",
]
