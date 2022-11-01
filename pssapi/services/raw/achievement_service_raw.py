"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import AchievementDesign as _AchievementDesign


# ---------- Constants ----------

LIST_ACHIEVEMENT_DESIGNS_2_BASE_PATH: str = 'AchievementService/ListAchievementDesigns2'


# ---------- Endpoints ----------

async def list_achievement_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_AchievementDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
        **params
    }
    result = await _core.get_entities_from_path(_AchievementDesign, 'AchievementDesigns', production_server, LIST_ACHIEVEMENT_DESIGNS_2_BASE_PATH, **params)
    return result
