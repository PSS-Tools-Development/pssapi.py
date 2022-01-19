"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ConditionTypeRaw:
    XML_NODE_NAME: str = "ConditionType"

    def __init__(self, condition_type_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._color_string: str = _parse.pss_str(condition_type_info.get("ColorString"))
        self._condition_type_availability: int = _parse.pss_int(condition_type_info.get("ConditionTypeAvailability"))
        self._condition_type_category: str = _parse.pss_str(condition_type_info.get("ConditionTypeCategory"))
        self._condition_type_comparison: str = _parse.pss_str(condition_type_info.get("ConditionTypeComparison"))
        self._condition_type_description: str = _parse.pss_str(condition_type_info.get("ConditionTypeDescription"))
        self._condition_type_id: int = _parse.pss_int(condition_type_info.get("ConditionTypeId"))
        self._condition_type_key: str = _parse.pss_str(condition_type_info.get("ConditionTypeKey"))
        self._condition_type_name: str = _parse.pss_str(condition_type_info.get("ConditionTypeName"))
        self._condition_type_parameter: str = _parse.pss_str(condition_type_info.get("ConditionTypeParameter"))
        self._condition_type_parameter_value: int = _parse.pss_int(condition_type_info.get("ConditionTypeParameterValue"))
        self._image_sprite_id: int = _parse.pss_int(condition_type_info.get("ImageSpriteId"))
        self._order_index: int = _parse.pss_int(condition_type_info.get("OrderIndex"))
        self._required_research_design_id: int = _parse.pss_int(condition_type_info.get("RequiredResearchDesignId"))
        self._room_category_type: str = _parse.pss_str(condition_type_info.get("RoomCategoryType"))
        self._room_type: str = _parse.pss_str(condition_type_info.get("RoomType"))

    @property
    def color_string(self) -> str:
        return self._color_string

    @property
    def condition_type_availability(self) -> int:
        return self._condition_type_availability

    @property
    def condition_type_category(self) -> str:
        return self._condition_type_category

    @property
    def condition_type_comparison(self) -> str:
        return self._condition_type_comparison

    @property
    def condition_type_description(self) -> str:
        return self._condition_type_description

    @property
    def condition_type_id(self) -> int:
        return self._condition_type_id

    @property
    def condition_type_key(self) -> str:
        return self._condition_type_key

    @property
    def condition_type_name(self) -> str:
        return self._condition_type_name

    @property
    def condition_type_parameter(self) -> str:
        return self._condition_type_parameter

    @property
    def condition_type_parameter_value(self) -> int:
        return self._condition_type_parameter_value

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
            self.color_string,
            self.condition_type_availability,
            self.condition_type_category,
            self.condition_type_comparison,
            self.condition_type_description,
            self.condition_type_id,
            self.condition_type_key,
            self.condition_type_name,
            self.condition_type_parameter,
            self.condition_type_parameter_value,
            self.image_sprite_id,
            self.order_index,
            self.required_research_design_id,
            self.room_category_type,
            self.room_type,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ColorString": self.color_string,
                "ConditionTypeAvailability": self.condition_type_availability,
                "ConditionTypeCategory": self.condition_type_category,
                "ConditionTypeComparison": self.condition_type_comparison,
                "ConditionTypeDescription": self.condition_type_description,
                "ConditionTypeId": self.condition_type_id,
                "ConditionTypeKey": self.condition_type_key,
                "ConditionTypeName": self.condition_type_name,
                "ConditionTypeParameter": self.condition_type_parameter,
                "ConditionTypeParameterValue": self.condition_type_parameter_value,
                "ImageSpriteId": self.image_sprite_id,
                "OrderIndex": self.order_index,
                "RequiredResearchDesignId": self.required_research_design_id,
                "RoomCategoryType": self.room_category_type,
                "RoomType": self.room_type,
            }

        return self._dict
