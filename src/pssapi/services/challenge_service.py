from typing import List as _List

from .raw import ChallengeServiceRaw as _ChallengeServiceRaw
import pssapi.services.service_base as _service_base
from ..entities import ChallengeDesign as _ChallengeDesign


class ChallengeService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint('ChallengeDesignVersion')
    async def list_all_challenge_designs(self, design_version: int = None) -> _List[_ChallengeDesign]:
        production_server = await self.get_production_server()
        result = await _ChallengeServiceRaw.list_all_challenge_designs_2(production_server, design_version, self.language_key)
        return result
