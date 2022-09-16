####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import Battle as _Battle



# ---------- Constants ----------

LIST_MISSION_BATTLES_BASE_PATH: str = 'BattleService/ListMissionBattles'
LIST_PV_P_BATTLES_BASE_PATH: str = 'BattleService/ListPvPBattles'


# ---------- Endpoints ----------

async def list_mission_battles(production_server: str, take: int, skip: int, access_token: str, client_date_time: _datetime, **params) -> _List[_Battle]:
    params = {
        'take': take,
        'skip': skip,
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_Battle, 'Battles', production_server, LIST_MISSION_BATTLES_BASE_PATH, **params)
    return result


async def list_pv_p_battles(production_server: str, take: int, skip: int, access_token: str, client_date_time: _datetime, **params) -> _List[_Battle]:
    params = {
        'take': take,
        'skip': skip,
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_Battle, 'Battles', production_server, LIST_PV_P_BATTLES_BASE_PATH, **params)
    return result


