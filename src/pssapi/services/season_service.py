import datetime as _datetime
from typing import List as _List

import pssapi.services.service_base as _service_base

from .. import utils as _utils
from ..entities import SeasonDesign as _SeasonDesign
from .raw import SeasonServiceRaw as _SeasonServiceRaw


class SeasonService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("SeasonDesignVersion")
    async def list_all_season_designs(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_SeasonDesign]:
        production_server = await self.get_production_server()
        result = await _SeasonServiceRaw.list_all_season_designs(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version, self.language_key)
        return result
