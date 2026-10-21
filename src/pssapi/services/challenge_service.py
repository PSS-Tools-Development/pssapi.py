import datetime as _datetime
from typing import List as _List

import pssapi.services.service_base as _service_base

from .. import utils as _utils
from ..entities import ChallengeDesign as _ChallengeDesign
from .raw import ChallengeServiceRaw as _ChallengeServiceRaw


class ChallengeService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("ChallengeDesignVersion")
    async def list_all_challenge_designs(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_ChallengeDesign]:
        """Return all challenge designs (challenge event blueprints with entry fee, prize, and lives) from the versioned catalog.

        Challenges are either AI events or War Games currently. Check :attr:`pssapi.enums.ChallengeType` on each
        design to see which kind a given challenge is.
        """
        production_server = await self.get_production_server()
        result = await _ChallengeServiceRaw.list_all_challenge_designs_2(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version, self.language_key)
        return result
