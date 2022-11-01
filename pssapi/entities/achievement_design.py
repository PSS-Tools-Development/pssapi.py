
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AchievementDesignRaw as _AchievementDesignRaw
from ..types import EntityInfo as _EntityInfo


class AchievementDesign(_EntityWithIdBase, _AchievementDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<AchievementDesign {self.id}>'

    def __str__(self) -> str:
        return f'<AchievementDesign {self.id}>'

    @property
    def id(self) -> int:
        return self.achievement_design_id
