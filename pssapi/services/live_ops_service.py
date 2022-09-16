from typing import List as _List

from .raw import LiveOpsServiceRaw as _LiveOpsServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import LiveOps as _LiveOps


class LiveOpsService(_ServiceBase):
    async def get_today_live_ops(self, language_key: str, device_type: str) -> _List[_LiveOps]:
        raise NotImplemented()
        result = await _LiveOpsServiceRaw.get_today_live_ops(self.production_server, language_key: str, device_type: str)
        return result


