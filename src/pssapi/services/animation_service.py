import datetime as _datetime
from typing import List as _List

import pssapi.services.service_base as _service_base

from .. import utils as _utils
from ..entities import Animation as _Animation
from .raw import AnimationServiceRaw as _AnimationServiceRaw


class AnimationService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("AnimationVersion")
    async def list_animations(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_Animation]:
        production_server = await self.get_production_server()
        result = await _AnimationServiceRaw.list_animations(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version)
        return result
