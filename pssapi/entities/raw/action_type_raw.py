"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ActionTypeRaw:
    XML_NODE_NAME: str = 'ActionType'

    def __init__(self, action_type_info: _EntityInfo) -> None:
        self.__color_string: str = _parse.pss_str(
            action_type_info.get('ColorString'))
        self.__action_type_id: int = _parse.pss_int(
            action_type_info.get('ActionTypeId'))
        self.__image_sprite_id: int = _parse.pss_int(
            action_type_info.get('ImageSpriteId'))
        self.__required_research_design_id: int = _parse.pss_int(
            action_type_info.get('RequiredResearchDesignId'))
        self.__order_index: int = _parse.pss_int(
            action_type_info.get('OrderIndex'))
        self.__action_type_category: str = _parse.pss_str(
            action_type_info.get('ActionTypeCategory'))
        self.__condition_type_category: str = _parse.pss_str(
            action_type_info.get('ConditionTypeCategory'))
        self.__condition_type_parameter: str = _parse.pss_str(
            action_type_info.get('ConditionTypeParameter'))
        self.__action_type_description: str = _parse.pss_str(
            action_type_info.get('ActionTypeDescription'))
        self.__action_type_key: str = _parse.pss_str(
            action_type_info.get('ActionTypeKey'))
        self.__action_type_parameter_value: int = _parse.pss_int(
            action_type_info.get('ActionTypeParameterValue'))
        self.__room_type: str = _parse.pss_str(
            action_type_info.get('RoomType'))
        self.__action_type_parameter_relativity: str = _parse.pss_str(
            action_type_info.get('ActionTypeParameterRelativity'))
        self.__action_type_name: str = _parse.pss_str(
            action_type_info.get('ActionTypeName'))

    @property
    def color_string(self) -> str:
        return self.__color_string

    @property
    def action_type_id(self) -> int:
        return self.__action_type_id

    @property
    def image_sprite_id(self) -> int:
        return self.__image_sprite_id

    @property
    def required_research_design_id(self) -> int:
        return self.__required_research_design_id

    @property
    def order_index(self) -> int:
        return self.__order_index

    @property
    def action_type_category(self) -> str:
        return self.__action_type_category

    @property
    def condition_type_category(self) -> str:
        return self.__condition_type_category

    @property
    def condition_type_parameter(self) -> str:
        return self.__condition_type_parameter

    @property
    def action_type_description(self) -> str:
        return self.__action_type_description

    @property
    def action_type_key(self) -> str:
        return self.__action_type_key

    @property
    def action_type_parameter_value(self) -> int:
        return self.__action_type_parameter_value

    @property
    def room_type(self) -> str:
        return self.__room_type

    @property
    def action_type_parameter_relativity(self) -> str:
        return self.__action_type_parameter_relativity

    @property
    def action_type_name(self) -> str:
        return self.__action_type_name
