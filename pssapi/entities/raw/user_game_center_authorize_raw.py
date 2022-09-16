####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserGameCenterAuthorizeRaw():
    XML_NODE_NAME: str = 'UserGameCenterAuthorize'

    def __init__(self, user_game_center_authorize_info: _EntityInfo) -> None:
        self.__error_message: str = _parse.pss_str(user_game_center_authorize_info.get('errorMessage'))

    @property
    def error_message(self) -> str:
        return self.__error_message
