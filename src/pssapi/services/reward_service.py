from typing import List

from pssapi.services import service_base

from ..entities import RewardDesign
from .raw import RewardServiceRaw


class RewardService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("RewardDesignVersion")
    async def list_all_reward_designs(self, client_date_time: str, design_version: int = None) -> List[RewardDesign]:
        production_server = await self.get_production_server()
        result = await RewardServiceRaw.list_all_reward_designs_2(production_server, client_date_time, design_version, self.language_key)
        return result
