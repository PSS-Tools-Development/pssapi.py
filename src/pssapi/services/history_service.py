from pssapi.services import service_base

from ..entities import History
from .raw import HistoryServiceRaw


class HistoryService(service_base.ServiceBase):
    async def price_history(self, item_design_id: int) -> History:
        production_server = await self.get_production_server()
        result = await HistoryServiceRaw.price_history(production_server, item_design_id)
        return result
