from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import TrainingDesignRaw as _TrainingDesignRaw


class TrainingDesign(_TrainingDesignRaw, _EntityWithIdBase):
    def __init__(self, training_design_info: _EntityInfo) -> None:
        super().__init__(training_design_info)
        self._training_animation_style_enum: _enums.TrainingAnimationStyle = _parse.pss_str_enum(self.training_animation_style, _enums.TrainingAnimationStyle)

    @property
    def id(self) -> int:
        return self.training_design_id

    @property
    def training_animation_style_enum(self) -> "_enums.TrainingAnimationStyle":
        return self._training_animation_style_enum
