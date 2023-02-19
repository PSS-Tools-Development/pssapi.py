
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AchievementDesignRaw as _AchievementDesignRaw
from ..types import EntityInfo as _EntityInfo


class AchievementDesign(_AchievementDesignRaw, _EntityWithIdBase):
    def __init__(self, achievement_design_info: _EntityInfo) -> None:
        super().__init__(achievement_design_info)

    @property
    def id(self) -> int:
        return self.achievement_design_id
