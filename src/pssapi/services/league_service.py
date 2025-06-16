import datetime as _datetime
from typing import List as _List

import pssapi.services.service_base as _service_base

from .. import utils as _utils
from ..entities import League as _League
from .raw import LeagueServiceRaw as _LeagueServiceRaw


class LeagueService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("LeagueVersion")
    async def list_leagues(self, access_token: str, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_League]:
        production_server = await self.get_production_server()
        result = await _LeagueServiceRaw.list_leagues_2(production_server, access_token, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version, self.language_key)
        return result
