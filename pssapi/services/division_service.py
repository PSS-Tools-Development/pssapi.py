from typing import List as _List

from .raw import DivisionServiceRaw as _DivisionServiceRaw
import pssapi.services.service_base as _service_base
from ..entities import DivisionDesign as _DivisionDesign


class DivisionService(_service_base.ServiceBase):
    async def list_all_division_designs(self, design_version: int = None) -> _List[_DivisionDesign]:
        production_server = await self.get_production_server()
        result = await _DivisionServiceRaw.list_all_division_designs_2(production_server, design_version, self.language_key)
        return result
