"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class AnimationRaw:
    XML_NODE_NAME: str = 'Animation'

    def __init__(self, animation_info: _EntityInfo) -> None:
        self.__key: str = _parse.pss_str(animation_info.get('Key'))
        self.__animation_effect_type: str = _parse.pss_str(
            animation_info.get('AnimationEffectType'))
        self.__animation_sprites: str = _parse.pss_str(
            animation_info.get('AnimationSprites'))
        self.__duration: int = _parse.pss_int(animation_info.get('Duration'))
        self.__animation_id: int = _parse.pss_int(
            animation_info.get('AnimationId'))

    @property
    def key(self) -> str:
        return self.__key

    @property
    def animation_effect_type(self) -> str:
        return self.__animation_effect_type

    @property
    def animation_sprites(self) -> str:
        return self.__animation_sprites

    @property
    def duration(self) -> int:
        return self.__duration

    @property
    def animation_id(self) -> int:
        return self.__animation_id
