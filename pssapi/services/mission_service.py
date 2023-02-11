from typing import List as _List
from typing import Tuple as _Tuple

from .raw import MissionServiceRaw as _MissionServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import MissionDesign as _MissionDesign


class MissionService(_ServiceBase):
    async def list_all_mission_designs(self, design_version: int = None) -> _List[_MissionDesign]:
        production_server = await self.get_production_server()
        result = await _MissionServiceRaw.list_all_mission_designs_4(production_server, design_version, self.language_key)
        return result

