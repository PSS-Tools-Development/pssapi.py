"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import AchievementDesign as _AchievementDesign

# ---------- Constants ----------

LIST_ACHIEVEMENT_DESIGNS_2_BASE_PATH: str = "AchievementService/ListAchievementDesigns2"


# ---------- Endpoints ----------


async def list_achievement_designs_2(production_server: str, design_version: int, language_key: str, **params) -> _List[_AchievementDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await _core.get_entities_from_path(((_AchievementDesign, "AchievementDesigns", True),), "AchievementDesigns", production_server, LIST_ACHIEVEMENT_DESIGNS_2_BASE_PATH, "GET", **params)
    return result
