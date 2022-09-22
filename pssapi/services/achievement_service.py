from typing import List as _List

from .raw import AchievementServiceRaw as _AchievementServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import AchievementDesign as _AchievementDesign


class AchievementService(_ServiceBase, _AchievementServiceRaw):
    async def list_achievement_designs_2(self, design_version: int = None, **params) -> _List[_AchievementDesign]:
        return await self._list_achievement_designs_2(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<AchievementService: {self.name}>'

    def __str__(self) -> str:
        return f'<AchievementService: {self.name}>'
