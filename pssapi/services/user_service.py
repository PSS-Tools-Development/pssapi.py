from datetime import datetime as _datetime
from typing import List as _List

from .raw import UserServiceRaw as _UserServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import User as _User
from ...entities import HeartBeat as _HeartBeat
from ...entities import UserLogin as _UserLogin
from ...entities import UserGameCenterAuthorize as _UserGameCenterAuthorize
from ...entities import ListFriends as _ListFriends


class UserService(_ServiceBase):
    async def add_gamecenter_friends(self, gamecenter_friend_ids: int, access_token: str) -> _List[_User]:
        raise NotImplemented()
        result = await _UserServiceRaw.add_gamecenter_friends(self.production_server, gamecenter_friend_ids: int, access_token: str)
        return result


    async def authorize_firebase_token(self, device_key: str, firebase_token: str, access_token: str) -> _List[_User]:
        raise NotImplemented()
        result = await _UserServiceRaw.authorize_firebase_token(self.production_server, device_key: str, firebase_token: str, access_token: str)
        return result


    async def device_login_12(self, ) -> _List[_UserLogin]:
        raise NotImplemented()
        result = await _UserServiceRaw.device_login_12(self.production_server, )
        return result


    async def heart_beat_4(self, checksum: int, access_token: str, client_date_time: _datetime) -> _List[_HeartBeat]:
        raise NotImplemented()
        result = await _UserServiceRaw.heart_beat_4(self.production_server, checksum: int, access_token: str, client_date_time: _datetime)
        return result


    async def list_friends(self, user_id: int, access_token: str) -> _List[_ListFriends]:
        raise NotImplemented()
        result = await _UserServiceRaw.list_friends(self.production_server, user_id: int, access_token: str)
        return result


    async def user_game_center_authorize(self, game_center_id: str, game_center_name: str, device_key: str, access_token: str) -> _List[_UserGameCenterAuthorize]:
        raise NotImplemented()
        result = await _UserServiceRaw.user_game_center_authorize(self.production_server, game_center_id: str, game_center_name: str, device_key: str, access_token: str)
        return result


