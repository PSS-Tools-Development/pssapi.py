from typing import List as _List

from .raw import DivisionServiceRaw as _DivisionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import DivisionDesign as _DivisionDesign


class DivisionService(_ServiceBase, _DivisionServiceRaw):
    async def list_all_division_designs_2(self, design_version: int = None, **params) -> _List[_DivisionDesign]:
        return await self._list_all_division_designs_2(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<DivisionService: {self.name}>'

    def __str__(self) -> str:
        return f'<DivisionService: {self.name}>'
