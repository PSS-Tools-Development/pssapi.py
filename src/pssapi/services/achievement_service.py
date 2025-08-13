from typing import List

from pssapi.services import service_base

from ..entities import AchievementDesign
from .raw import AchievementServiceRaw


class AchievementService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("AchievementDesignVersion")
    async def list_achievement_designs(self, design_version: int = None) -> List[AchievementDesign]:
        production_server = await self.get_production_server()
        result = await AchievementServiceRaw.list_achievement_designs_2(production_server, design_version, self.language_key)
        return result
