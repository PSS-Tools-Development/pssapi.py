from typing import List as _List

from .raw import AchievementServiceRaw as _AchievementServiceRaw
import pssapi.services.service_base as _service_base
from ..entities import AchievementDesign as _AchievementDesign


class AchievementService(_service_base.ServiceBase):
    async def list_achievement_designs(self, design_version: int = None) -> _List[_AchievementDesign]:
        production_server = await self.get_production_server()
        result = await _AchievementServiceRaw.list_achievement_designs_2(production_server, design_version, self.language_key)
        return result
