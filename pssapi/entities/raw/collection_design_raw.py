"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CollectionDesignRaw:
    XML_NODE_NAME: str = 'CollectionDesign'

    def __init__(self, collection_design_info: _EntityInfo) -> None:
        self.base_enhancement_value: int = _parse.pss_int(
            collection_design_info.get('BaseEnhancementValue'))
        self.collection_description: str = _parse.pss_str(
            collection_design_info.get('CollectionDescription'))
        self.collection_design_id: int = _parse.pss_int(
            collection_design_info.get('CollectionDesignId'))
        self.collection_name: str = _parse.pss_str(
            collection_design_info.get('CollectionName'))
        self.collection_type: str = _parse.pss_str(
            collection_design_info.get('CollectionType'))
        self.color_string: str = _parse.pss_str(
            collection_design_info.get('ColorString'))
        self.enhancement_type: str = _parse.pss_str(
            collection_design_info.get('EnhancementType'))
        self.flags: int = _parse.pss_int(collection_design_info.get('Flags'))
        self.halo_animation_id: int = _parse.pss_int(
            collection_design_info.get('HaloAnimationId'))
        self.icon_sprite_id: int = _parse.pss_int(
            collection_design_info.get('IconSpriteId'))
        self.max_combo: int = _parse.pss_int(
            collection_design_info.get('MaxCombo'))
        self.min_combo: int = _parse.pss_int(
            collection_design_info.get('MinCombo'))
        self.sprite_id: int = _parse.pss_int(
            collection_design_info.get('SpriteId'))
        self.step_enhancement_value: int = _parse.pss_int(
            collection_design_info.get('StepEnhancementValue'))
