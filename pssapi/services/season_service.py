from typing import List as _List

from .raw import SeasonServiceRaw as _SeasonServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import SeasonDesign as _SeasonDesign


class SeasonService(_ServiceBase):
    async def list_all_season_designs(self, : None, language_key: str, design_version: int) -> _List[_SeasonDesign]:
        raise NotImplemented()
        result = await _SeasonServiceRaw.list_all_season_designs(self.production_server, : None, language_key: str, design_version: int)
        return result


