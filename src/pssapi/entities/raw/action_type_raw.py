"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class ActionTypeRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "ActionType"

    def __init__(self, action_type_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._action_type_category: str = _parse.pss_str(action_type_info.pop("ActionTypeCategory", None))
        self._action_type_description: str = _parse.pss_str(action_type_info.pop("ActionTypeDescription", None))
        self._action_type_id: int = _parse.pss_int(action_type_info.pop("ActionTypeId", None))
        self._action_type_key: str = _parse.pss_str(action_type_info.pop("ActionTypeKey", None))
        self._action_type_name: str = _parse.pss_str(action_type_info.pop("ActionTypeName", None))
        self._action_type_parameter_relativity: str = _parse.pss_str(action_type_info.pop("ActionTypeParameterRelativity", None))
        self._action_type_parameter_value: int = _parse.pss_int(action_type_info.pop("ActionTypeParameterValue", None))
        self._color_string: str = _parse.pss_str(action_type_info.pop("ColorString", None))
        self._condition_parameter_argument: int = _parse.pss_int(action_type_info.pop("ConditionParameterArgument", None))
        self._condition_type_category: str = _parse.pss_str(action_type_info.pop("ConditionTypeCategory", None))
        self._condition_type_parameter: str = _parse.pss_str(action_type_info.pop("ConditionTypeParameter", None))
        self._image_sprite_id: int = _parse.pss_int(action_type_info.pop("ImageSpriteId", None))
        self._order_index: int = _parse.pss_int(action_type_info.pop("OrderIndex", None))
        self._required_research_design_id: int = _parse.pss_int(action_type_info.pop("RequiredResearchDesignId", None))
        self._room_category_type: str = _parse.pss_str(action_type_info.pop("RoomCategoryType", None))
        self._room_type: str = _parse.pss_str(action_type_info.pop("RoomType", None))
        super().__init__(action_type_info)

    @property
    def action_type_category(self) -> str:
        return self._action_type_category

    @property
    def action_type_description(self) -> str:
        return self._action_type_description

    @property
    def action_type_id(self) -> int:
        return self._action_type_id

    @property
    def action_type_key(self) -> str:
        return self._action_type_key

    @property
    def action_type_name(self) -> str:
        return self._action_type_name

    @property
    def action_type_parameter_relativity(self) -> str:
        return self._action_type_parameter_relativity

    @property
    def action_type_parameter_value(self) -> int:
        return self._action_type_parameter_value

    @property
    def color_string(self) -> str:
        return self._color_string

    @property
    def condition_parameter_argument(self) -> int:
        return self._condition_parameter_argument

    @property
    def condition_type_category(self) -> str:
        return self._condition_type_category

    @property
    def condition_type_parameter(self) -> str:
        return self._condition_type_parameter

    @property
    def image_sprite_id(self) -> int:
        return self._image_sprite_id

    @property
    def order_index(self) -> int:
        return self._order_index

    @property
    def required_research_design_id(self) -> int:
        return self._required_research_design_id

    @property
    def room_category_type(self) -> str:
        return self._room_category_type

    @property
    def room_type(self) -> str:
        return self._room_type

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

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ActionTypeCategory": self.action_type_category,
                "ActionTypeDescription": self.action_type_description,
                "ActionTypeId": self.action_type_id,
                "ActionTypeKey": self.action_type_key,
                "ActionTypeName": self.action_type_name,
                "ActionTypeParameterRelativity": self.action_type_parameter_relativity,
                "ActionTypeParameterValue": self.action_type_parameter_value,
                "ColorString": self.color_string,
                "ConditionParameterArgument": self.condition_parameter_argument,
                "ConditionTypeCategory": self.condition_type_category,
                "ConditionTypeParameter": self.condition_type_parameter,
                "ImageSpriteId": self.image_sprite_id,
                "OrderIndex": self.order_index,
                "RequiredResearchDesignId": self.required_research_design_id,
                "RoomCategoryType": self.room_category_type,
                "RoomType": self.room_type,
            }
            self._dict.update(super().__dict__())

        return self._dict
