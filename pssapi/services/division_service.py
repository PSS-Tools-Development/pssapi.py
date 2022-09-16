from typing import List as _List

from .raw import DivisionServiceRaw as _DivisionServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import DivisionDesign as _DivisionDesign


class DivisionService(_ServiceBase):
    async def list_all_division_designs_2(self, language_key: str, design_version: int) -> _List[_DivisionDesign]:
        raise NotImplemented()
        result = await _DivisionServiceRaw.list_all_division_designs_2(self.production_server, language_key: str, design_version: int)
        return result


