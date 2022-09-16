from datetime import datetime as _datetime
from typing import List as _List

from .raw import MissionServiceRaw as _MissionServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import MissionDesign as _MissionDesign
from ...entities import MissionEvent as _MissionEvent


class MissionService(_ServiceBase):
    async def list_all_mission_designs_4(self, language_key: str, design_version: int) -> _List[_MissionDesign]:
        raise NotImplemented()
        result = await _MissionServiceRaw.list_all_mission_designs_4(self.production_server, language_key: str, design_version: int)
        return result


    async def list_completed_mission_events(self, client_date_time: _datetime, checksum: str, access_token: str) -> _List[_MissionEvent]:
        raise NotImplemented()
        result = await _MissionServiceRaw.list_completed_mission_events(self.production_server, client_date_time: _datetime, checksum: str, access_token: str)
        return result


