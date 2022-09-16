####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import MissionDesign as _MissionDesign
from ...entities import MissionEvent as _MissionEvent



# ---------- Constants ----------

LIST_ALL_MISSION_DESIGNS_4_BASE_PATH: str = 'MissionService/ListAllMissionDesigns4'
LIST_COMPLETED_MISSION_EVENTS_BASE_PATH: str = 'MissionService/ListCompletedMissionEvents'


# ---------- Endpoints ----------

async def list_all_mission_designs_4(production_server: str, language_key: str, design_version: int, **params) -> _List[_MissionDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_MissionDesign, 'MissionDesigns', production_server, LIST_ALL_MISSION_DESIGNS_4_BASE_PATH, **params)
    return result


async def list_completed_mission_events(production_server: str, client_date_time: _datetime, checksum: str, access_token: str, **params) -> _List[_MissionEvent]:
    params = {
        'clientDateTime': client_date_time,
        'checksum': checksum,
        'accessToken': access_token,
    }
    result = await _core.get_entities_from_path(_MissionEvent, 'MissionEvents', production_server, LIST_COMPLETED_MISSION_EVENTS_BASE_PATH, **params)
    return result


