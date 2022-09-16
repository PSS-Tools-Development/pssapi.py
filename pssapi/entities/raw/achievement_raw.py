####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class AchievementRaw():
    XML_NODE_NAME: str = 'Achievement'

    def __init__(self, achievement_info: _EntityInfo) -> None:
        self.__achievement_id: int = _parse.pss_int(achievement_info.get('AchievementId'))
        self.__achievement_design_id: int = _parse.pss_int(achievement_info.get('AchievementDesignId'))
        self.__user_id: int = _parse.pss_int(achievement_info.get('UserId'))
        self.__progress_value: int = _parse.pss_int(achievement_info.get('ProgressValue'))
        self.__collected: bool = _parse.pss_bool(achievement_info.get('Collected'))

    @property
    def achievement_id(self) -> int:
        return self.__achievement_id

    @property
    def achievement_design_id(self) -> int:
        return self.__achievement_design_id

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def progress_value(self) -> int:
        return self.__progress_value

    @property
    def collected(self) -> bool:
        return self.__collected
