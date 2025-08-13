"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import AchievementDesign


# ---------- Constants ----------

LIST_ACHIEVEMENT_DESIGNS_2_BASE_PATH: str = "AchievementService/ListAchievementDesigns2"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_achievement_designs_2(production_server: str, design_version: int, language_key: str, **params) -> List[AchievementDesign]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(
        ((AchievementDesign, "AchievementDesigns", True),), "AchievementDesigns", production_server, LIST_ACHIEVEMENT_DESIGNS_2_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result
