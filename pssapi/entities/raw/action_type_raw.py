"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ActionTypeRaw:
    XML_NODE_NAME: str = 'ActionType'

    def __init__(self, action_type_info: _EntityInfo) -> None:
        self.action_type_category: str = _parse.pss_str(
            action_type_info.get('ActionTypeCategory'))
        self.action_type_description: str = _parse.pss_str(
            action_type_info.get('ActionTypeDescription'))
        self.action_type_id: int = _parse.pss_int(
            action_type_info.get('ActionTypeId'))
        self.action_type_key: str = _parse.pss_str(
            action_type_info.get('ActionTypeKey'))
        self.action_type_name: str = _parse.pss_str(
            action_type_info.get('ActionTypeName'))
        self.action_type_parameter_relativity: str = _parse.pss_str(
            action_type_info.get('ActionTypeParameterRelativity'))
        self.action_type_parameter_value: int = _parse.pss_int(
            action_type_info.get('ActionTypeParameterValue'))
        self.color_string: str = _parse.pss_str(
            action_type_info.get('ColorString'))
        self.condition_type_category: str = _parse.pss_str(
            action_type_info.get('ConditionTypeCategory'))
        self.condition_type_parameter: str = _parse.pss_str(
            action_type_info.get('ConditionTypeParameter'))
        self.image_sprite_id: int = _parse.pss_int(
            action_type_info.get('ImageSpriteId'))
        self.order_index: int = _parse.pss_int(
            action_type_info.get('OrderIndex'))
        self.required_research_design_id: int = _parse.pss_int(
            action_type_info.get('RequiredResearchDesignId'))
        self.room_type: str = _parse.pss_str(action_type_info.get('RoomType'))
