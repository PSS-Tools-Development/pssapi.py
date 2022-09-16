####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CollectionDesignRaw():
    XML_NODE_NAME: str = 'CollectionDesign'

    def __init__(self, collection_design_info: _EntityInfo) -> None:
        self.__collection_design_id: int = _parse.pss_int(collection_design_info.get('CollectionDesignId'))
        self.__collection_name: str = _parse.pss_str(collection_design_info.get('CollectionName'))
        self.__min_combo: int = _parse.pss_int(collection_design_info.get('MinCombo'))
        self.__max_combo: int = _parse.pss_int(collection_design_info.get('MaxCombo'))
        self.__enhancement_type: str = _parse.pss_str(collection_design_info.get('EnhancementType'))
        self.__base_enhancement_value: int = _parse.pss_int(collection_design_info.get('BaseEnhancementValue'))
        self.__flags: int = _parse.pss_int(collection_design_info.get('Flags'))
        self.__collection_type: str = _parse.pss_str(collection_design_info.get('CollectionType'))
        self.__collection_description: str = _parse.pss_str(collection_design_info.get('CollectionDescription'))
        self.__sprite_id: int = _parse.pss_int(collection_design_info.get('SpriteId'))
        self.__color_string: str = _parse.pss_str(collection_design_info.get('ColorString'))
        self.__step_enhancement_value: int = _parse.pss_int(collection_design_info.get('StepEnhancementValue'))
        self.__icon_sprite_id: int = _parse.pss_int(collection_design_info.get('IconSpriteId'))
        self.__halo_animation_id: int = _parse.pss_int(collection_design_info.get('HaloAnimationId'))

    @property
    def collection_design_id(self) -> int:
        return self.__collection_design_id

    @property
    def collection_name(self) -> str:
        return self.__collection_name

    @property
    def min_combo(self) -> int:
        return self.__min_combo

    @property
    def max_combo(self) -> int:
        return self.__max_combo

    @property
    def enhancement_type(self) -> str:
        return self.__enhancement_type

    @property
    def base_enhancement_value(self) -> int:
        return self.__base_enhancement_value

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def collection_type(self) -> str:
        return self.__collection_type

    @property
    def collection_description(self) -> str:
        return self.__collection_description

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id

    @property
    def color_string(self) -> str:
        return self.__color_string

    @property
    def step_enhancement_value(self) -> int:
        return self.__step_enhancement_value

    @property
    def icon_sprite_id(self) -> int:
        return self.__icon_sprite_id

    @property
    def halo_animation_id(self) -> int:
        return self.__halo_animation_id
