"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserMarkerRaw:
    XML_NODE_NAME: str = 'UserMarker'

    def __init__(self, user_marker_info: _EntityInfo) -> None:
        self.__user_marker_id: int = _parse.pss_int(
            user_marker_info.get('UserMarkerId'))
        self.__user_id: int = _parse.pss_int(user_marker_info.get('UserId'))
        self.__star_system_marker_id: int = _parse.pss_int(
            user_marker_info.get('StarSystemMarkerId'))
        self.__purchase_flags: int = _parse.pss_int(
            user_marker_info.get('PurchaseFlags'))
        self.__marker_progress_value: int = _parse.pss_int(
            user_marker_info.get('MarkerProgressValue'))
        self.__is_collected: bool = _parse.pss_bool(
            user_marker_info.get('IsCollected'))
        self.__last_update_date: datetime = _parse.pss_datetime(
            user_marker_info.get('LastUpdateDate'))

    @property
    def user_marker_id(self) -> int:
        return self.__user_marker_id

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def star_system_marker_id(self) -> int:
        return self.__star_system_marker_id

    @property
    def purchase_flags(self) -> int:
        return self.__purchase_flags

    @property
    def marker_progress_value(self) -> int:
        return self.__marker_progress_value

    @property
    def is_collected(self) -> bool:
        return self.__is_collected

    @property
    def last_update_date(self) -> datetime:
        return self.__last_update_date
