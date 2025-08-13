from .entity_base import EntityWithIdBase
from .raw import AchievementDesignRaw


class AchievementDesign(AchievementDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.achievement_design_id


__all__ = [
    "AchievementDesign",
]
