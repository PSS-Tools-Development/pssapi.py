"""
    This file has been generated automatically
"""

from typing import List as _List
from typing import Tuple as _Tuple

from ... import core as _core
from ...entities import Research as _Research
from ...entities import ResearchDesign as _ResearchDesign
from ...entities import User as _User

# ---------- Constants ----------

LIST_ALL_RESEARCH_DESIGNS_2_BASE_PATH: str = "ResearchService/ListAllResearchDesigns2"
SPEED_UP_RESEARCH_USING_BOOST_GAUGE_BASE_PATH: str = "ResearchService/SpeedUpResearchUsingBoostGauge"


# ---------- Endpoints ----------


async def list_all_research_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_ResearchDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_ResearchDesign, "ResearchDesigns", True),), "ResearchDesigns", production_server, LIST_ALL_RESEARCH_DESIGNS_2_BASE_PATH, "GET", **params)
    return result


async def speed_up_research_using_boost_gauge(production_server: str, access_token: str, client_date_time: str, research_id: int, **params) -> _Tuple[_Research, _User]:
    params = {"accessToken": access_token, "clientDateTime": client_date_time, "researchId": research_id, **params}
    result = await _core.get_entities_from_path(
        ((_Research, "Research", False), (_User, "User", False)), "SpeedUpResearchUsingBoostGauge", production_server, SPEED_UP_RESEARCH_USING_BOOST_GAUGE_BASE_PATH, "POST", **params
    )
    return result
