from typing import List as _List

from .raw import DivisionServiceRaw as _DivisionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import DivisionDesign as _DivisionDesign


class DivisionService(_ServiceBase, _DivisionServiceRaw):
    async def list_all_division_designs_2(self, **params) -> _List[_DivisionDesign]:
        return self._list_all_division_designs_2(self.production_server, self.language_key, **params)

    def __repr__(self) -> str:
        return f'<DivisionService: {self.name}>'

    def __str__(self) -> str:
        return f'<DivisionService: {self.name}>'
