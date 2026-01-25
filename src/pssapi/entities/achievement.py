from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AchievementRaw as _AchievementRaw


class Achievement(_AchievementRaw, _EntityWithIdBase):
    def __init__(self, achievement_info: _EntityInfo) -> None:
        super().__init__(achievement_info)

    @property
    def id(self) -> int:
        return self.achievement_id
