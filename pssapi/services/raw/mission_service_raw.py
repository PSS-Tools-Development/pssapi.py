"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import MissionDesign as _MissionDesign

# ---------- Constants ----------

LIST_ALL_MISSION_DESIGNS_4_BASE_PATH: str = 'MissionService/ListAllMissionDesigns4'


# ---------- Endpoints ----------

async def list_all_mission_designs_4(production_server: str, language_key: str, design_version: int, **params) -> _List[_MissionDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path(_MissionDesign, 'MissionDesigns', production_server, LIST_ALL_MISSION_DESIGNS_4_BASE_PATH, **params)
    return result
