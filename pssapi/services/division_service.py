from typing import List as _List

from .raw import DivisionServiceRaw as _DivisionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import DivisionDesign as _DivisionDesign


class DivisionService(_ServiceBase):
    async def list_all_division_designs(self, design_version: int = None) -> _List[_DivisionDesign]:
        result = await _DivisionServiceRaw.list_all_division_designs_2(self.production_server, design_version, self.language_key)
        return result
