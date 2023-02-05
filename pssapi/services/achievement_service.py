from typing import List as _List

from .raw import AchievementServiceRaw as _AchievementServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import AchievementDesign as _AchievementDesign


class AchievementService(_ServiceBase):
    async def list_achievement_designs(self, design_version: int = None) -> _List[_AchievementDesign]:
        result = await _AchievementServiceRaw.list_achievement_designs_2((await self.get_production_server()), design_version, self.language_key)
        return result
