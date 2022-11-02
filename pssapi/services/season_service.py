from typing import List as _List

from .raw import SeasonServiceRaw as _SeasonServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import SeasonDesign as _SeasonDesign


class SeasonService(_ServiceBase):
    async def list_all_season_designs(self, design_version: int = None) -> _List[_SeasonDesign]:
        result = await _SeasonServiceRaw.list_all_season_designs(production_server=self.production_server, design_version=design_version, language_key=self.language_key)
        return result
