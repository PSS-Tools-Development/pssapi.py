from typing import List as _List

from .raw import AchievementServiceRaw as _AchievementServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import AchievementDesign as _AchievementDesign


class AchievementService(_ServiceBase, _AchievementServiceRaw):
    async def list_achievement_designs_2(self, **params) -> _List[_AchievementDesign]:
        return self._list_achievement_designs_2(self.production_server, self.language_key, **params)

    def __repr__(self) -> str:
        return f'<AchievementService: {self.name}>'

    def __str__(self) -> str:
        return f'<AchievementService: {self.name}>'
