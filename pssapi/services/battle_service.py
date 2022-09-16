from datetime import datetime as _datetime
from typing import List as _List

from .raw import BattleServiceRaw as _BattleServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import Battle as _Battle


class BattleService(_ServiceBase):
    async def list_mission_battles(self, take: int, skip: int, access_token: str, client_date_time: _datetime) -> _List[_Battle]:
        raise NotImplemented()
        result = await _BattleServiceRaw.list_mission_battles(self.production_server, take: int, skip: int, access_token: str, client_date_time: _datetime)
        return result


    async def list_pv_p_battles(self, take: int, skip: int, access_token: str, client_date_time: _datetime) -> _List[_Battle]:
        raise NotImplemented()
        result = await _BattleServiceRaw.list_pv_p_battles(self.production_server, take: int, skip: int, access_token: str, client_date_time: _datetime)
        return result


