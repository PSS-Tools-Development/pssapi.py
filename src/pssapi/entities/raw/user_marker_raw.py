"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class UserMarkerRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "UserMarker"

    def __init__(self, user_marker_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._is_collected: bool = _parse.pss_bool(user_marker_info.pop("IsCollected", None))
        self._last_update_date: _datetime = _parse.pss_datetime(user_marker_info.pop("LastUpdateDate", None))
        self._marker_progress_value: int = _parse.pss_int(user_marker_info.pop("MarkerProgressValue", None))
        self._purchase_flags: int = _parse.pss_int(user_marker_info.pop("PurchaseFlags", None))
        self._star_system_marker_id: int = _parse.pss_int(user_marker_info.pop("StarSystemMarkerId", None))
        self._user_id: int = _parse.pss_int(user_marker_info.pop("UserId", None))
        self._user_marker_id: int = _parse.pss_int(user_marker_info.pop("UserMarkerId", None))
        super().__init__(user_marker_info)

    @property
    def is_collected(self) -> bool:
        return self._is_collected

    @property
    def last_update_date(self) -> _datetime:
        return self._last_update_date

    @property
    def marker_progress_value(self) -> int:
        return self._marker_progress_value

    @property
    def purchase_flags(self) -> int:
        return self._purchase_flags

    @property
    def star_system_marker_id(self) -> int:
        return self._star_system_marker_id

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def user_marker_id(self) -> int:
        return self._user_marker_id

    def _key(self):
        return (
            self.is_collected,
            self.last_update_date,
            self.marker_progress_value,
            self.purchase_flags,
            self.star_system_marker_id,
            self.user_id,
            self.user_marker_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "IsCollected": self.is_collected,
                "LastUpdateDate": self.last_update_date,
                "MarkerProgressValue": self.marker_progress_value,
                "PurchaseFlags": self.purchase_flags,
                "StarSystemMarkerId": self.star_system_marker_id,
                "UserId": self.user_id,
                "UserMarkerId": self.user_marker_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
