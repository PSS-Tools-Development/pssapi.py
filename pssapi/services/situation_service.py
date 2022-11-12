from typing import List as _List

from .raw import SituationServiceRaw as _SituationServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import SituationDesign as _SituationDesign


class SituationService(_ServiceBase):
    async def list_situation_designs(self, design_version: int = None) -> _List[_SituationDesign]:
        result = await _SituationServiceRaw.list_situation_designs(self.production_server, design_version, self.language_key)
        return result
