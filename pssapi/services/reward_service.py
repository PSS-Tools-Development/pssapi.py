from typing import List as _List

from .raw import RewardServiceRaw as _RewardServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import RewardDesign as _RewardDesign


class RewardService(_ServiceBase):
    async def list_all_reward_designs(self, design_version: int = None) -> _List[_RewardDesign]:
        result = await _RewardServiceRaw.list_all_reward_designs_2(self.production_server, self.language_key, design_version)
        return result
