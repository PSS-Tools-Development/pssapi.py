####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomDesignSpriteRaw():
    XML_NODE_NAME: str = 'RoomDesignSprite'

    def __init__(self, room_design_sprite_info: _EntityInfo) -> None:
        self.__room_design_sprite_id: int = _parse.pss_int(room_design_sprite_info.get('RoomDesignSpriteId'))
        self.__room_design_id: int = _parse.pss_int(room_design_sprite_info.get('RoomDesignId'))
        self.__sprite_id: int = _parse.pss_int(room_design_sprite_info.get('SpriteId'))
        self.__room_sprite_type: str = _parse.pss_str(room_design_sprite_info.get('RoomSpriteType'))
        self.__room_effect_type: str = _parse.pss_str(room_design_sprite_info.get('RoomEffectType'))
        self.__room_effect_parameter: int = _parse.pss_int(room_design_sprite_info.get('RoomEffectParameter'))
        self.__skin_name: str = _parse.pss_str(room_design_sprite_info.get('SkinName'))
        self.__skin_description: str = _parse.pss_str(room_design_sprite_info.get('SkinDescription'))
        self.__requirement_string: str = _parse.pss_str(room_design_sprite_info.get('RequirementString'))
        self.__flags: int = _parse.pss_int(room_design_sprite_info.get('Flags'))
        self.__race_id: int = _parse.pss_int(room_design_sprite_info.get('RaceId'))
        self.__animation_id: int = _parse.pss_int(room_design_sprite_info.get('AnimationId'))
        self.__skin_key: int = _parse.pss_int(room_design_sprite_info.get('SkinKey'))

    @property
    def room_design_sprite_id(self) -> int:
        return self.__room_design_sprite_id

    @property
    def room_design_id(self) -> int:
        return self.__room_design_id

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id

    @property
    def room_sprite_type(self) -> str:
        return self.__room_sprite_type

    @property
    def room_effect_type(self) -> str:
        return self.__room_effect_type

    @property
    def room_effect_parameter(self) -> int:
        return self.__room_effect_parameter

    @property
    def skin_name(self) -> str:
        return self.__skin_name

    @property
    def skin_description(self) -> str:
        return self.__skin_description

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def race_id(self) -> int:
        return self.__race_id

    @property
    def animation_id(self) -> int:
        return self.__animation_id

    @property
    def skin_key(self) -> int:
        return self.__skin_key
