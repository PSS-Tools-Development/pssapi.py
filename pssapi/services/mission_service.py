from typing import List as _List

from .raw import MissionServiceRaw as _MissionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import MissionDesign as _MissionDesign


class MissionService(_ServiceBase, _MissionServiceRaw):
    async def list_all_mission_designs_4(self, **params) -> _List[_MissionDesign]:
        return self._list_all_mission_designs_4(self.production_server, self.language_key, self.design_version, **params)

    def __repr__(self) -> str:
        return f'<MissionService: {self.name}>'

    def __str__(self) -> str:
        return f'<MissionService: {self.name}>'
