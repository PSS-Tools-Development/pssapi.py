"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict
from typing import List as _List

import pssapi.entities as _entities

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class DefendingEngagementGroupRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "DefendingEngagementGroup"

    def __init__(self, defending_engagement_group_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._engagement_group_id: int = _parse.pss_int(defending_engagement_group_info.pop("EngagementGroupId", None))
        self._engagement_group_icon_sprite_id: int = _parse.pss_int(defending_engagement_group_info.pop("EngagementGroupIconSpriteId", None))
        self._engagement_group_name: str = _parse.pss_str(defending_engagement_group_info.pop("EngagementGroupName", None))
        self._engagement_group_users: _List[_entities.EngagementGroupUser] = (
            [_entities.EngagementGroupUser(child_info) for child_info in defending_engagement_group_info.pop("EngagementGroupUsers")[0].get("EngagementGroupUser", [])]
            if defending_engagement_group_info.get("EngagementGroupUsers")
            else []
        )
        self._engagement_id: int = _parse.pss_int(defending_engagement_group_info.pop("EngagementId", None))
        self._power_limit: int = _parse.pss_int(defending_engagement_group_info.pop("PowerLimit", None))
        self._requires_approval: bool = _parse.pss_bool(defending_engagement_group_info.pop("RequiresApproval", None))
        self._update_date: _datetime = _parse.pss_datetime(defending_engagement_group_info.pop("UpdateDate", None))
        self._user_limit: int = _parse.pss_int(defending_engagement_group_info.pop("UserLimit", None))
        super().__init__(defending_engagement_group_info)

    @property
    def engagement_group_id(self) -> int:
        return self._engagement_group_id

    @property
    def engagement_group_icon_sprite_id(self) -> int:
        return self._engagement_group_icon_sprite_id

    @property
    def engagement_group_name(self) -> str:
        return self._engagement_group_name

    @property
    def engagement_group_users(self) -> _List["_entities.EngagementGroupUser"]:
        return self._engagement_group_users

    @property
    def engagement_id(self) -> int:
        return self._engagement_id

    @property
    def power_limit(self) -> int:
        return self._power_limit

    @property
    def requires_approval(self) -> bool:
        return self._requires_approval

    @property
    def update_date(self) -> _datetime:
        return self._update_date

    @property
    def user_limit(self) -> int:
        return self._user_limit

    def _key(self):
        return (
            self.engagement_group_id,
            self.engagement_group_icon_sprite_id,
            self.engagement_group_name,
            tuple(child._key() for child in self.engagement_group_users),
            self.engagement_id,
            self.power_limit,
            self.requires_approval,
            self.update_date,
            self.user_limit,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "EngagementGroupId": self.engagement_group_id,
                "EngagementGroupIconSpriteId": self.engagement_group_icon_sprite_id,
                "EngagementGroupName": self.engagement_group_name,
                "EngagementGroupUsers": [dict(child) for child in self.engagement_group_users],
                "EngagementId": self.engagement_id,
                "PowerLimit": self.power_limit,
                "RequiresApproval": self.requires_approval,
                "UpdateDate": self.update_date,
                "UserLimit": self.user_limit,
            }
            self._dict.update(super().__dict__())

        return self._dict
