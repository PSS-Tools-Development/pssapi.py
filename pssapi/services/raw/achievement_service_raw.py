####################################################
##   This file has been generated automatically   ##
####################################################

from datetime import datetime as _datetime
from typing import List as _List

from ... import core as _core
from ...entities import Achievement as _Achievement
from ...entities import AchievementDesign as _AchievementDesign



# ---------- Constants ----------

LIST_ACHIEVEMENT_DESIGNS_2_BASE_PATH: str = 'AchievementService/ListAchievementDesigns2'
LIST_ACHIEVEMENTS_OF_A_USER_BASE_PATH: str = 'AchievementService/ListAchievementsOfAUser'


# ---------- Endpoints ----------

async def list_achievement_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_AchievementDesign]:
    params = {
        'languageKey': language_key,
        'designVersion': design_version,
    }
    result = await _core.get_entities_from_path(_AchievementDesign, 'AchievementDesigns', production_server, LIST_ACHIEVEMENT_DESIGNS_2_BASE_PATH, **params)
    return result


async def list_achievements_of_a_user(production_server: str, access_token: str, client_date_time: _datetime, **params) -> _List[_Achievement]:
    params = {
        'accessToken': access_token,
        'clientDateTime': client_date_time,
    }
    result = await _core.get_entities_from_path(_Achievement, 'Achievements', production_server, LIST_ACHIEVEMENTS_OF_A_USER_BASE_PATH, **params)
    return result


