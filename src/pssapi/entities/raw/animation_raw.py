"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class AnimationRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Animation"

    def __init__(self, animation_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._animation_effect_type: str = _parse.pss_str(animation_info.pop("AnimationEffectType", None))
        self._animation_id: int = _parse.pss_int(animation_info.pop("AnimationId", None))
        self._animation_sprites: str = _parse.pss_str(animation_info.pop("AnimationSprites", None))
        self._duration: int = _parse.pss_int(animation_info.pop("Duration", None))
        self._key: str = _parse.pss_str(animation_info.pop("Key", None))
        super().__init__(animation_info)

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
            self._dict.update(super().__dict__())

        return self._dict
