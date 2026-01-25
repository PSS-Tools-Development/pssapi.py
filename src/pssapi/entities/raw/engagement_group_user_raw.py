"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

import pssapi.entities as _entities

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class EngagementGroupUserRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "EngagementGroupUser"

    def __init__(self, engagement_group_user_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._approval_state: str = _parse.pss_str(engagement_group_user_info.pop("ApprovalState", None))
        self._attacked_engagement_group_user_ids: str = _parse.pss_str(engagement_group_user_info.pop("AttackedEngagementGroupUserIds", None))
        self._attacks_used: int = _parse.pss_int(engagement_group_user_info.pop("AttacksUsed", None))
        self._engagement_group_id: int = _parse.pss_int(engagement_group_user_info.pop("EngagementGroupId", None))
        self._engagement_group_user_id: int = _parse.pss_int(engagement_group_user_info.pop("EngagementGroupUserId", None))
        self._engagement_group_user_name: str = _parse.pss_str(engagement_group_user_info.pop("EngagementGroupUserName", None))
        self._engagement_group_user_state: str = _parse.pss_str(engagement_group_user_info.pop("EngagementGroupUserState", None))
        self._hp: float = _parse.pss_float(engagement_group_user_info.pop("Hp", None))
        self._lives_used: int = _parse.pss_int(engagement_group_user_info.pop("LivesUsed", None))
        self._max_attacks: int = _parse.pss_int(engagement_group_user_info.pop("MaxAttacks", None))
        self._max_lives: int = _parse.pss_int(engagement_group_user_info.pop("MaxLives", None))
        self._power_score: int = _parse.pss_int(engagement_group_user_info.pop("PowerScore", None))
        self._score: int = _parse.pss_int(engagement_group_user_info.pop("Score", None))
        self._ship_design_id: int = _parse.pss_int(engagement_group_user_info.pop("ShipDesignId", None))
        self._update_date: _datetime = _parse.pss_datetime(engagement_group_user_info.pop("UpdateDate", None))
        self._user: _entities.User = _entities.User(engagement_group_user_info.pop("User")[0]) if engagement_group_user_info.get("User", []) else None
        self._user_id: int = _parse.pss_int(engagement_group_user_info.pop("UserId", None))
        self._user_type: str = _parse.pss_str(engagement_group_user_info.pop("UserType", None))
        super().__init__(engagement_group_user_info)

    @property
    def approval_state(self) -> str:
        return self._approval_state

    @property
    def attacked_engagement_group_user_ids(self) -> str:
        return self._attacked_engagement_group_user_ids

    @property
    def attacks_used(self) -> int:
        return self._attacks_used

    @property
    def engagement_group_id(self) -> int:
        return self._engagement_group_id

    @property
    def engagement_group_user_id(self) -> int:
        return self._engagement_group_user_id

    @property
    def engagement_group_user_name(self) -> str:
        return self._engagement_group_user_name

    @property
    def engagement_group_user_state(self) -> str:
        return self._engagement_group_user_state

    @property
    def hp(self) -> float:
        return self._hp

    @property
    def lives_used(self) -> int:
        return self._lives_used

    @property
    def max_attacks(self) -> int:
        return self._max_attacks

    @property
    def max_lives(self) -> int:
        return self._max_lives

    @property
    def power_score(self) -> int:
        return self._power_score

    @property
    def score(self) -> int:
        return self._score

    @property
    def ship_design_id(self) -> int:
        return self._ship_design_id

    @property
    def update_date(self) -> _datetime:
        return self._update_date

    @property
    def user(self) -> "_entities.User":
        return self._user

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def user_type(self) -> str:
        return self._user_type

    def _key(self):
        return (
            self.approval_state,
            self.attacked_engagement_group_user_ids,
            self.attacks_used,
            self.engagement_group_id,
            self.engagement_group_user_id,
            self.engagement_group_user_name,
            self.engagement_group_user_state,
            self.hp,
            self.lives_used,
            self.max_attacks,
            self.max_lives,
            self.power_score,
            self.score,
            self.ship_design_id,
            self.update_date,
            self.user._key() if self.user else None,
            self.user_id,
            self.user_type,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ApprovalState": self.approval_state,
                "AttackedEngagementGroupUserIds": self.attacked_engagement_group_user_ids,
                "AttacksUsed": self.attacks_used,
                "EngagementGroupId": self.engagement_group_id,
                "EngagementGroupUserId": self.engagement_group_user_id,
                "EngagementGroupUserName": self.engagement_group_user_name,
                "EngagementGroupUserState": self.engagement_group_user_state,
                "Hp": self.hp,
                "LivesUsed": self.lives_used,
                "MaxAttacks": self.max_attacks,
                "MaxLives": self.max_lives,
                "PowerScore": self.power_score,
                "Score": self.score,
                "ShipDesignId": self.ship_design_id,
                "UpdateDate": self.update_date,
                "User": dict(self.user) if self.user else None,
                "UserId": self.user_id,
                "UserType": self.user_type,
            }
            self._dict.update(super().__dict__())

        return self._dict
