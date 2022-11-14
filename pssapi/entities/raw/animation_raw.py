"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class AnimationRaw:
    XML_NODE_NAME: str = 'Animation'

    def __init__(self, animation_info: _EntityInfo) -> None:
        self.animation_effect_type: str = _parse.pss_str(animation_info.get('AnimationEffectType'))
        self.animation_id: int = _parse.pss_int(animation_info.get('AnimationId'))
        self.animation_sprites: str = _parse.pss_str(animation_info.get('AnimationSprites'))
        self.duration: int = _parse.pss_int(animation_info.get('Duration'))
        self.key: str = _parse.pss_str(animation_info.get('Key'))
