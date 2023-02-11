from typing import List as _List
from typing import Tuple as _Tuple

from .raw import SituationServiceRaw as _SituationServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import SituationDesign as _SituationDesign


class SituationService(_ServiceBase):
    async def list_situation_designs(self, design_version: int = None) -> _List[_SituationDesign]:
        production_server = await self.get_production_server()
        result = await _SituationServiceRaw.list_situation_designs(production_server, design_version, self.language_key)
        return result

