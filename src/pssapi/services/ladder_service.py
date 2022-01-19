from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import User as _User
from .raw import LadderServiceRaw as _LadderServiceRaw


class LadderService(_service_base.ServiceBase):
    async def list_users_by_championship_score_ranking(self, access_token: str, from_: int, to: int) -> _List[_User]:
        production_server = await self.get_production_server()
        result = await _LadderServiceRaw.list_users_by_championship_score_ranking(production_server, access_token, from_, to)
        return result

    async def list_users_by_ranking(self, access_token: str, from_: int, to: int, to_100: str) -> _List[_User]:
        production_server = await self.get_production_server()
        result = await _LadderServiceRaw.list_users_by_ranking(production_server, access_token, from_, to, to_100)
        return result
