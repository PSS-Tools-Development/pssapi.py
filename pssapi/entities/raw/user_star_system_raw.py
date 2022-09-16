####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserStarSystemRaw():
    XML_NODE_NAME: str = 'UserStarSystem'

    def __init__(self, user_star_system_info: _EntityInfo) -> None:
        self.__user_star_system_id: int = _parse.pss_int(user_star_system_info.get('UserStarSystemId'))
        self.__star_system_id: int = _parse.pss_int(user_star_system_info.get('StarSystemId'))
        self.__exploration_percentage: int = _parse.pss_int(user_star_system_info.get('ExplorationPercentage'))
        self.__user_id: int = _parse.pss_int(user_star_system_info.get('UserId'))

    @property
    def user_star_system_id(self) -> int:
        return self.__user_star_system_id

    @property
    def star_system_id(self) -> int:
        return self.__star_system_id

    @property
    def exploration_percentage(self) -> int:
        return self.__exploration_percentage

    @property
    def user_id(self) -> int:
        return self.__user_id
