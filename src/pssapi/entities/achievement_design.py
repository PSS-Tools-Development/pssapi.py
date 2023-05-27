from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AchievementDesignRaw as _AchievementDesignRaw


class AchievementDesign(_AchievementDesignRaw, _EntityWithIdBase):
    def __init__(self, achievement_design_info: _EntityInfo) -> None:
        super().__init__(achievement_design_info)
        self._achievement_type_enum: _enums.AchievementType = _parse.pss_str_enum(self.achievement_type, _enums.AchievementType)
        self._duration_type_enum: _enums.DurationType = _parse.pss_str_enum(self.duration_type, _enums.DurationType)
        self._guide_type_enum: _enums.GuideType = _parse.pss_str_enum(self.guide_type, _enums.GuideType)

    @property
    def id(self) -> int:
        return self.achievement_design_id

    @property
    def achievement_type_enum(self) -> "_enums.AchievementType":
        return self._achievement_type_enum

    @property
    def duration_type_enum(self) -> "_enums.DurationType":
        return self._duration_type_enum

    @property
    def guide_type_enum(self) -> "_enums.GuideType":
        return self._guide_type_enum
