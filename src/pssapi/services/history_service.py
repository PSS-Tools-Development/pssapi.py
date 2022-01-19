import pssapi.services.service_base as _service_base

from ..entities import History as _History
from .raw import HistoryServiceRaw as _HistoryServiceRaw


class HistoryService(_service_base.ServiceBase):
    async def price_history(self, item_design_id: int) -> _History:
        production_server = await self.get_production_server()
        result = await _HistoryServiceRaw.price_history(production_server, item_design_id)
        return result
