####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ConditionTypeRaw():
    XML_NODE_NAME: str = 'ConditionType'

    def __init__(self, condition_type_info: _EntityInfo) -> None:
        self.__condition_type_id: int = _parse.pss_int(condition_type_info.get('ConditionTypeId'))
        self.__condition_type_name: str = _parse.pss_str(condition_type_info.get('ConditionTypeName'))
        self.__condition_type_description: str = _parse.pss_str(condition_type_info.get('ConditionTypeDescription'))
        self.__condition_type_availability: int = _parse.pss_int(condition_type_info.get('ConditionTypeAvailability'))
        self.__condition_type_category: str = _parse.pss_str(condition_type_info.get('ConditionTypeCategory'))
        self.__condition_type_comparison: str = _parse.pss_str(condition_type_info.get('ConditionTypeComparison'))
        self.__condition_type_parameter_value: int = _parse.pss_int(condition_type_info.get('ConditionTypeParameterValue'))
        self.__condition_type_key: str = _parse.pss_str(condition_type_info.get('ConditionTypeKey'))
        self.__image_sprite_id: int = _parse.pss_int(condition_type_info.get('ImageSpriteId'))
        self.__room_type: str = _parse.pss_str(condition_type_info.get('RoomType'))
        self.__condition_type_parameter: str = _parse.pss_str(condition_type_info.get('ConditionTypeParameter'))
        self.__color_string: str = _parse.pss_str(condition_type_info.get('ColorString'))
        self.__required_research_design_id: int = _parse.pss_int(condition_type_info.get('RequiredResearchDesignId'))
        self.__order_index: int = _parse.pss_int(condition_type_info.get('OrderIndex'))

    @property
    def condition_type_id(self) -> int:
        return self.__condition_type_id

    @property
    def condition_type_name(self) -> str:
        return self.__condition_type_name

    @property
    def condition_type_description(self) -> str:
        return self.__condition_type_description

    @property
    def condition_type_availability(self) -> int:
        return self.__condition_type_availability

    @property
    def condition_type_category(self) -> str:
        return self.__condition_type_category

    @property
    def condition_type_comparison(self) -> str:
        return self.__condition_type_comparison

    @property
    def condition_type_parameter_value(self) -> int:
        return self.__condition_type_parameter_value

    @property
    def condition_type_key(self) -> str:
        return self.__condition_type_key

    @property
    def image_sprite_id(self) -> int:
        return self.__image_sprite_id

    @property
    def room_type(self) -> str:
        return self.__room_type

    @property
    def condition_type_parameter(self) -> str:
        return self.__condition_type_parameter

    @property
    def color_string(self) -> str:
        return self.__color_string

    @property
    def required_research_design_id(self) -> int:
        return self.__required_research_design_id

    @property
    def order_index(self) -> int:
        return self.__order_index
