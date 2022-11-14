"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserMarkerRaw:
    XML_NODE_NAME: str = 'UserMarker'

    def __init__(self, user_marker_info: _EntityInfo) -> None:
        self.is_collected: bool = _parse.pss_bool(user_marker_info.get('IsCollected'))
        self.last_update_date: _datetime = _parse.pss_datetime(user_marker_info.get('LastUpdateDate'))
        self.marker_progress_value: int = _parse.pss_int(user_marker_info.get('MarkerProgressValue'))
        self.purchase_flags: int = _parse.pss_int(user_marker_info.get('PurchaseFlags'))
        self.star_system_marker_id: int = _parse.pss_int(user_marker_info.get('StarSystemMarkerId'))
        self.user_id: int = _parse.pss_int(user_marker_info.get('UserId'))
        self.user_marker_id: int = _parse.pss_int(user_marker_info.get('UserMarkerId'))
