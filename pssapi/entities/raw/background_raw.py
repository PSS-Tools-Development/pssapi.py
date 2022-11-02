"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class BackgroundRaw:
    XML_NODE_NAME: str = 'Background'

    def __init__(self, background_info: _EntityInfo) -> None:
        self.__hazard_category: str = _parse.pss_str(
            background_info.get('HazardCategory'))
        self.__close_object_sprite_id: str = _parse.pss_str(
            background_info.get('CloseObjectSpriteId'))
        self.__medium_object_sprite_id: str = _parse.pss_str(
            background_info.get('MediumObjectSpriteId'))
        self.__background_type: str = _parse.pss_str(
            background_info.get('BackgroundType'))
        self.__hazard_type: str = _parse.pss_str(
            background_info.get('HazardType'))
        self.__far_object_sprite_id: str = _parse.pss_str(
            background_info.get('FarObjectSpriteId'))
        self.__background_id: int = _parse.pss_int(
            background_info.get('BackgroundId'))
        self.__max_hazard_interval: int = _parse.pss_int(
            background_info.get('MaxHazardInterval'))
        self.__orbit_animation_id: int = _parse.pss_int(
            background_info.get('OrbitAnimationId'))
        self.__environment_type: str = _parse.pss_str(
            background_info.get('EnvironmentType'))
        self.__min_hazard_interval: int = _parse.pss_int(
            background_info.get('MinHazardInterval'))
        self.__hazard_chance: int = _parse.pss_int(
            background_info.get('HazardChance'))
        self.__hazard_argument: int = _parse.pss_int(
            background_info.get('HazardArgument'))
        self.__background_sprite_id: int = _parse.pss_int(
            background_info.get('BackgroundSpriteId'))
        self.__hazard_icon_sprite_id: int = _parse.pss_int(
            background_info.get('HazardIconSpriteId'))
        self.__is_active: bool = _parse.pss_bool(
            background_info.get('IsActive'))
        self.__environment_int_argument: int = _parse.pss_int(
            background_info.get('EnvironmentIntArgument'))
        self.__environment_float_argument: int = _parse.pss_int(
            background_info.get('EnvironmentFloatArgument'))
        self.__music_file_id: int = _parse.pss_int(
            background_info.get('MusicFileId'))
        self.__background_effect_type: str = _parse.pss_str(
            background_info.get('BackgroundEffectType'))
        self.__hazard_effect_sprite_id: int = _parse.pss_int(
            background_info.get('HazardEffectSpriteId'))
        self.__orbit_anchor_alignment: str = _parse.pss_str(
            background_info.get('OrbitAnchorAlignment'))

    @property
    def hazard_category(self) -> str:
        return self.__hazard_category

    @property
    def close_object_sprite_id(self) -> str:
        return self.__close_object_sprite_id

    @property
    def medium_object_sprite_id(self) -> str:
        return self.__medium_object_sprite_id

    @property
    def background_type(self) -> str:
        return self.__background_type

    @property
    def hazard_type(self) -> str:
        return self.__hazard_type

    @property
    def far_object_sprite_id(self) -> str:
        return self.__far_object_sprite_id

    @property
    def background_id(self) -> int:
        return self.__background_id

    @property
    def max_hazard_interval(self) -> int:
        return self.__max_hazard_interval

    @property
    def orbit_animation_id(self) -> int:
        return self.__orbit_animation_id

    @property
    def environment_type(self) -> str:
        return self.__environment_type

    @property
    def min_hazard_interval(self) -> int:
        return self.__min_hazard_interval

    @property
    def hazard_chance(self) -> int:
        return self.__hazard_chance

    @property
    def hazard_argument(self) -> int:
        return self.__hazard_argument

    @property
    def background_sprite_id(self) -> int:
        return self.__background_sprite_id

    @property
    def hazard_icon_sprite_id(self) -> int:
        return self.__hazard_icon_sprite_id

    @property
    def is_active(self) -> bool:
        return self.__is_active

    @property
    def environment_int_argument(self) -> int:
        return self.__environment_int_argument

    @property
    def environment_float_argument(self) -> int:
        return self.__environment_float_argument

    @property
    def music_file_id(self) -> int:
        return self.__music_file_id

    @property
    def background_effect_type(self) -> str:
        return self.__background_effect_type

    @property
    def hazard_effect_sprite_id(self) -> int:
        return self.__hazard_effect_sprite_id

    @property
    def orbit_anchor_alignment(self) -> str:
        return self.__orbit_anchor_alignment
