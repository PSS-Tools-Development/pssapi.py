from datetime import datetime as _datetime
from typing import List as _List

from .raw import AchievementServiceRaw as _AchievementServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import Achievement as _Achievement
from ...entities import AchievementDesign as _AchievementDesign


class AchievementService(_ServiceBase):
    async def list_achievement_designs_2(self, language_key: str, design_version: int) -> _List[_AchievementDesign]:
        raise NotImplemented()
        result = await _AchievementServiceRaw.list_achievement_designs_2(self.production_server, language_key: str, design_version: int)
        return result


    async def list_achievements_of_a_user(self, access_token: str, client_date_time: _datetime) -> _List[_Achievement]:
        raise NotImplemented()
        result = await _AchievementServiceRaw.list_achievements_of_a_user(self.production_server, access_token: str, client_date_time: _datetime)
        return result


