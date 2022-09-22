from typing import List as _List

from .raw import ChallengeServiceRaw as _ChallengeServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import ChallengeDesign as _ChallengeDesign


class ChallengeService(_ServiceBase, _ChallengeServiceRaw):
    async def list_all_challenge_designs_2(self, design_version: int = None, **params) -> _List[_ChallengeDesign]:
        return await self._list_all_challenge_designs_2(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<ChallengeService: {self.name}>'

    def __str__(self) -> str:
        return f'<ChallengeService: {self.name}>'
