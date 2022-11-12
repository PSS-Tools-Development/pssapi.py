"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ConditionTypeRaw:
    XML_NODE_NAME: str = 'ConditionType'

    def __init__(self, condition_type_info: _EntityInfo) -> None:
        self.color_string: str = _parse.pss_str(
            condition_type_info.get('ColorString'))
        self.condition_type_availability: int = _parse.pss_int(
            condition_type_info.get('ConditionTypeAvailability'))
        self.condition_type_category: str = _parse.pss_str(
            condition_type_info.get('ConditionTypeCategory'))
        self.condition_type_comparison: str = _parse.pss_str(
            condition_type_info.get('ConditionTypeComparison'))
        self.condition_type_description: str = _parse.pss_str(
            condition_type_info.get('ConditionTypeDescription'))
        self.condition_type_id: int = _parse.pss_int(
            condition_type_info.get('ConditionTypeId'))
        self.condition_type_key: str = _parse.pss_str(
            condition_type_info.get('ConditionTypeKey'))
        self.condition_type_name: str = _parse.pss_str(
            condition_type_info.get('ConditionTypeName'))
        self.condition_type_parameter: str = _parse.pss_str(
            condition_type_info.get('ConditionTypeParameter'))
        self.condition_type_parameter_value: int = _parse.pss_int(
            condition_type_info.get('ConditionTypeParameterValue'))
        self.image_sprite_id: int = _parse.pss_int(
            condition_type_info.get('ImageSpriteId'))
        self.order_index: int = _parse.pss_int(
            condition_type_info.get('OrderIndex'))
        self.required_research_design_id: int = _parse.pss_int(
            condition_type_info.get('RequiredResearchDesignId'))
        self.room_type: str = _parse.pss_str(
            condition_type_info.get('RoomType'))
