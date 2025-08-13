from typing import List, Tuple

from pssapi.services import service_base

from ..entities import Battle, MissionDesign, MissionEvent, User
from .raw import MissionServiceRaw


class MissionService(service_base.CacheableServiceBase):
    async def create_mission(self, access_token: str, checksum: str, client_date_time: str, message_id: int, mission_design_id: int) -> Tuple[Battle, MissionEvent, User, List[MissionEvent]]:
        production_server = await self.get_production_server()
        result = await MissionServiceRaw.create_mission_2(production_server, access_token, checksum, client_date_time, message_id, mission_design_id)
        return result

    @service_base.cache_endpoint("MissionDesignVersion")
    async def list_all_mission_designs(self, client_date_time: str, design_version: int = None) -> List[MissionDesign]:
        production_server = await self.get_production_server()
        result = await MissionServiceRaw.list_all_mission_designs_4(production_server, client_date_time, design_version, self.language_key)
        return result

    async def select_event(self, access_token: str, battle_id: int, checksum: str, client_date_time: str, client_number: int, mission_event_id: int) -> Tuple[Battle, User]:
        production_server = await self.get_production_server()
        result = await MissionServiceRaw.select_event_3(production_server, access_token, battle_id, checksum, client_date_time, client_number, mission_event_id)
        return result
