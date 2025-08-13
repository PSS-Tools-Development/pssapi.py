"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List, Tuple

from ... import core
from ...entities import Battle, MissionDesign, MissionEvent, User


# ---------- Constants ----------

CREATE_MISSION_2_BASE_PATH: str = "MissionService/CreateMission2"
LIST_ALL_MISSION_DESIGNS_4_BASE_PATH: str = "MissionService/ListAllMissionDesigns4"
SELECT_EVENT_2_BASE_PATH: str = "MissionService/SelectEvent2"
SELECT_EVENT_3_BASE_PATH: str = "MissionService/SelectEvent3"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def create_mission_2(
    production_server: str, access_token: str, checksum: str, client_date_time: str, message_id: int, mission_design_id: int, **params
) -> Tuple[Battle, MissionEvent, User, List[MissionEvent]]:
    params = {"accessToken": access_token, "checksum": checksum, "clientDateTime": client_date_time, "messageId": message_id, "missionDesignId": mission_design_id, **params}
    result = await core.get_entities_from_path(
        ((Battle, "Battle", False), (MissionEvent, "MissionEvent", False), (User, "User", False), (MissionEvent, "MissionEvents", True)),
        "CreateMission",
        production_server,
        CREATE_MISSION_2_BASE_PATH,
        "POST",
        response_gzipped=False,
        **params,
    )
    return result


async def list_all_mission_designs_4(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[MissionDesign]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(
        ((MissionDesign, "MissionDesigns", True),), "MissionDesigns", production_server, LIST_ALL_MISSION_DESIGNS_4_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result


async def select_event_2(production_server: str, access_token: str, battle_id: int, checksum: str, client_date_time: str, mission_event_id: int, **params) -> Battle:
    params = {"accessToken": access_token, "battleId": battle_id, "checksum": checksum, "clientDateTime": client_date_time, "missionEventId": mission_event_id, **params}
    result = await core.get_entities_from_path(((Battle, "Battle", False),), "SelectEvent", production_server, SELECT_EVENT_2_BASE_PATH, "POST", response_gzipped=False, **params)
    return result


async def select_event_3(production_server: str, access_token: str, battle_id: int, checksum: str, client_date_time: str, client_number: int, mission_event_id: int, **params) -> Tuple[Battle, User]:
    params = {"accessToken": access_token, "battleId": battle_id, "checksum": checksum, "clientDateTime": client_date_time, "clientNumber": client_number, "missionEventId": mission_event_id, **params}
    result = await core.get_entities_from_path(((Battle, "Battle", False), (User, "User", False)), "SelectEvent", production_server, SELECT_EVENT_3_BASE_PATH, "POST", response_gzipped=False, **params)
    return result
