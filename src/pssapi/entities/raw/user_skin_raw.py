"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class UserSkinRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "UserSkin"

    def __init__(self, user_skin_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._date_updated: _datetime = _parse.pss_datetime(user_skin_info.pop("DateUpdated", None))
        self._skin_set_id: int = _parse.pss_int(user_skin_info.pop("SkinSetId", None))
        self._user_id: int = _parse.pss_int(user_skin_info.pop("UserId", None))
        self._user_skin_id: int = _parse.pss_int(user_skin_info.pop("UserSkinId", None))
        super().__init__(user_skin_info)

    @property
    def date_updated(self) -> _datetime:
        return self._date_updated

    @property
    def skin_set_id(self) -> int:
        return self._skin_set_id

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def user_skin_id(self) -> int:
        return self._user_skin_id

    def _key(self):
        return (
            self.date_updated,
            self.skin_set_id,
            self.user_id,
            self.user_skin_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "DateUpdated": self.date_updated,
                "SkinSetId": self.skin_set_id,
                "UserId": self.user_id,
                "UserSkinId": self.user_skin_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
