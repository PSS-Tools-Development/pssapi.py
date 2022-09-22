from typing import List as _List

from .raw import RewardServiceRaw as _RewardServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import RewardDesign as _RewardDesign


class RewardService(_ServiceBase, _RewardServiceRaw):
    async def list_all_reward_designs_2(self, design_version: int = None, **params) -> _List[_RewardDesign]:
        return await self._list_all_reward_designs_2(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<RewardService: {self.name}>'

    def __str__(self) -> str:
        return f'<RewardService: {self.name}>'
