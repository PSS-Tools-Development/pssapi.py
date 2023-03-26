from typing import List as _List
from typing import Tuple as _Tuple

import pssapi.services.service_base as _service_base

from ..entities import Battle as _Battle
from ..entities import MissionDesign as _MissionDesign
from ..entities import MissionEvent as _MissionEvent
from ..entities import User as _User
from .raw import MissionServiceRaw as _MissionServiceRaw


class MissionService(_service_base.CacheableServiceBase):
    async def create_mission(self, access_token: str, checksum: str, client_date_time: str, message_id: int, mission_design_id: int) -> _Tuple[_Battle, _MissionEvent, _User, _List[_MissionEvent]]:
        production_server = await self.get_production_server()
        result = await _MissionServiceRaw.create_mission_2(production_server, access_token, checksum, client_date_time, message_id, mission_design_id)
        return result

    @_service_base.cache_endpoint("MissionDesignVersion")
    async def list_all_mission_designs(self, design_version: int = None) -> _List[_MissionDesign]:
        production_server = await self.get_production_server()
        result = await _MissionServiceRaw.list_all_mission_designs_4(production_server, design_version, self.language_key)
        return result

    async def select_event(self, access_token: str, battle_id: int, checksum: str, client_date_time: str, client_number: int, mission_event_id: int) -> _Tuple[_Battle, _User]:
        production_server = await self.get_production_server()
        result = await _MissionServiceRaw.select_event_3(production_server, access_token, battle_id, checksum, client_date_time, client_number, mission_event_id)
        return result
