"""
    This file has been generated automatically
"""

from typing import List as _List
from typing import Tuple as _Tuple

from ... import core as _core
from ...entities import Battle as _Battle
from ...entities import MissionDesign as _MissionDesign
from ...entities import MissionEvent as _MissionEvent
from ...entities import User as _User

# ---------- Constants ----------

LIST_ALL_MISSION_DESIGNS_4_BASE_PATH: str = "MissionService/ListAllMissionDesigns4"
SELECT_INSTANT_MISSION_3_BASE_PATH: str = "MissionService/SelectInstantMission3"


# ---------- Endpoints ----------


async def list_all_mission_designs_4(production_server: str, design_version: int, language_key: str, **params) -> _List[_MissionDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_MissionDesign, "MissionDesigns", True),), "MissionDesigns", production_server, LIST_ALL_MISSION_DESIGNS_4_BASE_PATH, "GET", **params)
    return result


async def select_instant_mission_3(
    production_server: str, access_token: str, checksum: str, client_date_time: str, client_number: int, message_id: int, mission_design_id: int, mission_event_id: int, **params
) -> _Tuple[_Battle, _User, _List[_MissionEvent]]:
    params = {
        "accessToken": access_token,
        "checksum": checksum,
        "clientDateTime": client_date_time,
        "clientNumber": client_number,
        "messageId": message_id,
        "missionDesignId": mission_design_id,
        "missionEventId": mission_event_id,
        **params,
    }
    result = await _core.get_entities_from_path(
        ((_Battle, "Battle", False), (_User, "User", False), (_MissionEvent, "MissionEvents", True)), "SelectInstantMission", production_server, SELECT_INSTANT_MISSION_3_BASE_PATH, "POST", **params
    )
    return result
