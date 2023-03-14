from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import RewardDesign as _RewardDesign
from .raw import RewardServiceRaw as _RewardServiceRaw


class RewardService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("RewardDesignVersion")
    async def list_all_reward_designs(self, design_version: int = None) -> _List[_RewardDesign]:
        production_server = await self.get_production_server()
        result = await _RewardServiceRaw.list_all_reward_designs_2(production_server, design_version, self.language_key)
        return result
