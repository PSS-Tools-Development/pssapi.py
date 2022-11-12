"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserStarSystemRaw:
    XML_NODE_NAME: str = 'UserStarSystem'

    def __init__(self, user_star_system_info: _EntityInfo) -> None:
        self.exploration_percentage: int = _parse.pss_int(
            user_star_system_info.get('ExplorationPercentage'))
        self.star_system_id: int = _parse.pss_int(
            user_star_system_info.get('StarSystemId'))
        self.user_id: int = _parse.pss_int(user_star_system_info.get('UserId'))
        self.user_star_system_id: int = _parse.pss_int(
            user_star_system_info.get('UserStarSystemId'))
