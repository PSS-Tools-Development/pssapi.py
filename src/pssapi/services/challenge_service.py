from typing import List

from pssapi.services import service_base

from ..entities import ChallengeDesign
from .raw import ChallengeServiceRaw


class ChallengeService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("ChallengeDesignVersion")
    async def list_all_challenge_designs(self, client_date_time: str, design_version: int = None) -> List[ChallengeDesign]:
        production_server = await self.get_production_server()
        result = await ChallengeServiceRaw.list_all_challenge_designs_2(production_server, client_date_time, design_version, self.language_key)
        return result
