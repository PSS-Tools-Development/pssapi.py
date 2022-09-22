from typing import List as _List

from .raw import SituationServiceRaw as _SituationServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import SituationDesign as _SituationDesign


class SituationService(_ServiceBase, _SituationServiceRaw):
    async def list_situation_designs(self, design_version: int = None, **params) -> _List[_SituationDesign]:
        return await self._list_situation_designs(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<SituationService: {self.name}>'

    def __str__(self) -> str:
        return f'<SituationService: {self.name}>'
