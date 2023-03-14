"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class AnimationRaw:
    XML_NODE_NAME: str = "Animation"

    def __init__(self, animation_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._animation_effect_type: str = _parse.pss_str(animation_info.get("AnimationEffectType"))
        self._animation_id: int = _parse.pss_int(animation_info.get("AnimationId"))
        self._animation_sprites: str = _parse.pss_str(animation_info.get("AnimationSprites"))
        self._duration: int = _parse.pss_int(animation_info.get("Duration"))
        self._key: str = _parse.pss_str(animation_info.get("Key"))

    @property
    def animation_effect_type(self) -> str:
        return self._animation_effect_type

    @property
    def animation_id(self) -> int:
        return self._animation_id

    @property
    def animation_sprites(self) -> str:
        return self._animation_sprites

    @property
    def duration(self) -> int:
        return self._duration

    @property
    def key(self) -> str:
        return self._key

    def _key(self):
        return (
            self.animation_effect_type,
            self.animation_id,
            self.animation_sprites,
            self.duration,
            self.key,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AnimationEffectType": self.animation_effect_type,
                "AnimationId": self.animation_id,
                "AnimationSprites": self.animation_sprites,
                "Duration": self.duration,
                "Key": self.key,
            }

        return self._dict
