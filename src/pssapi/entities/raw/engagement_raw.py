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


class EngagementRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Engagement"

    def __init__(self, engagement_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._attacking_alliance_id: int = _parse.pss_int(engagement_info.pop("AttackingAllianceId", None))
        self._attacking_engagement_group: _entities.AttackingEngagementGroup = (
            _entities.AttackingEngagementGroup(engagement_info.pop("AttackingEngagementGroup")[0]) if engagement_info.get("AttackingEngagementGroup", []) else None
        )
        self._attacking_engagement_group_id: int = _parse.pss_int(engagement_info.pop("AttackingEngagementGroupId", None))
        self._attacking_engagement_group_name: str = _parse.pss_str(engagement_info.pop("AttackingEngagementGroupName", None))
        self._attacking_points: int = _parse.pss_int(engagement_info.pop("AttackingPoints", None))
        self._defending_alliance_id: int = _parse.pss_int(engagement_info.pop("DefendingAllianceId", None))
        self._defending_engagement_group: _entities.DefendingEngagementGroup = (
            _entities.DefendingEngagementGroup(engagement_info.pop("DefendingEngagementGroup")[0]) if engagement_info.get("DefendingEngagementGroup", []) else None
        )
        self._defending_engagement_group_id: int = _parse.pss_int(engagement_info.pop("DefendingEngagementGroupId", None))
        self._defending_engagement_group_name: str = _parse.pss_str(engagement_info.pop("DefendingEngagementGroupName", None))
        self._defending_points: str = _parse.pss_str(engagement_info.pop("DefendingPoints", None))
        self._end_date: _datetime = _parse.pss_datetime(engagement_info.pop("EndDate", None))
        self._engagement_id: int = _parse.pss_int(engagement_info.pop("EngagementId", None))
        self._engagement_type: str = _parse.pss_str(engagement_info.pop("EngagementType", None))
        self._outcome_type: str = _parse.pss_str(engagement_info.pop("OutcomeType", None))
        self._reward_string: str = _parse.pss_str(engagement_info.pop("RewardString", None))
        self._scoring_type: str = _parse.pss_str(engagement_info.pop("ScoringType", None))
        self._star_system_id: int = _parse.pss_int(engagement_info.pop("StarSystemId", None))
        self._start_date: _datetime = _parse.pss_datetime(engagement_info.pop("StartDate", None))
        super().__init__(engagement_info)

    @property
    def attacking_alliance_id(self) -> int:
        return self._attacking_alliance_id

    @property
    def attacking_engagement_group(self) -> "_entities.AttackingEngagementGroup":
        return self._attacking_engagement_group

    @property
    def attacking_engagement_group_id(self) -> int:
        return self._attacking_engagement_group_id

    @property
    def attacking_engagement_group_name(self) -> str:
        return self._attacking_engagement_group_name

    @property
    def attacking_points(self) -> int:
        return self._attacking_points

    @property
    def defending_alliance_id(self) -> int:
        return self._defending_alliance_id

    @property
    def defending_engagement_group(self) -> "_entities.DefendingEngagementGroup":
        return self._defending_engagement_group

    @property
    def defending_engagement_group_id(self) -> int:
        return self._defending_engagement_group_id

    @property
    def defending_engagement_group_name(self) -> str:
        return self._defending_engagement_group_name

    @property
    def defending_points(self) -> str:
        return self._defending_points

    @property
    def end_date(self) -> _datetime:
        return self._end_date

    @property
    def engagement_id(self) -> int:
        return self._engagement_id

    @property
    def engagement_type(self) -> str:
        return self._engagement_type

    @property
    def outcome_type(self) -> str:
        return self._outcome_type

    @property
    def reward_string(self) -> str:
        return self._reward_string

    @property
    def scoring_type(self) -> str:
        return self._scoring_type

    @property
    def star_system_id(self) -> int:
        return self._star_system_id

    @property
    def start_date(self) -> _datetime:
        return self._start_date

    def _key(self):
        return (
            self.attacking_alliance_id,
            self.attacking_engagement_group._key() if self.attacking_engagement_group else None,
            self.attacking_engagement_group_id,
            self.attacking_engagement_group_name,
            self.attacking_points,
            self.defending_alliance_id,
            self.defending_engagement_group._key() if self.defending_engagement_group else None,
            self.defending_engagement_group_id,
            self.defending_engagement_group_name,
            self.defending_points,
            self.end_date,
            self.engagement_id,
            self.engagement_type,
            self.outcome_type,
            self.reward_string,
            self.scoring_type,
            self.star_system_id,
            self.start_date,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AttackingAllianceId": self.attacking_alliance_id,
                "AttackingEngagementGroup": dict(self.attacking_engagement_group) if self.attacking_engagement_group else None,
                "AttackingEngagementGroupId": self.attacking_engagement_group_id,
                "AttackingEngagementGroupName": self.attacking_engagement_group_name,
                "AttackingPoints": self.attacking_points,
                "DefendingAllianceId": self.defending_alliance_id,
                "DefendingEngagementGroup": dict(self.defending_engagement_group) if self.defending_engagement_group else None,
                "DefendingEngagementGroupId": self.defending_engagement_group_id,
                "DefendingEngagementGroupName": self.defending_engagement_group_name,
                "DefendingPoints": self.defending_points,
                "EndDate": self.end_date,
                "EngagementId": self.engagement_id,
                "EngagementType": self.engagement_type,
                "OutcomeType": self.outcome_type,
                "RewardString": self.reward_string,
                "ScoringType": self.scoring_type,
                "StarSystemId": self.star_system_id,
                "StartDate": self.start_date,
            }
            self._dict.update(super().__dict__())

        return self._dict
