from typing import List as _List

from .raw import SeasonServiceRaw as _SeasonServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import SeasonDesign as _SeasonDesign


class SeasonService(_ServiceBase, _SeasonServiceRaw):
    async def list_all_season_designs(self, design_version: int = None, **params) -> _List[_SeasonDesign]:
        return await self._list_all_season_designs(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<SeasonService: {self.name}>'

    def __str__(self) -> str:
        return f'<SeasonService: {self.name}>'
