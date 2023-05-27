from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AnimationRaw as _AnimationRaw


class Animation(_AnimationRaw, _EntityWithIdBase):
    def __init__(self, animation_info: _EntityInfo) -> None:
        super().__init__(animation_info)
        self._animation_effect_type_enum: _enums.AnimationEffectType = _parse.pss_str_enum(self.animation_effect_type, _enums.AnimationEffectType)

    @property
    def id(self) -> int:
        return self.animation_id

    @property
    def animation_effect_type_enum(self) -> "_enums.AnimationEffectType":
        return self._animation_effect_type_enum
