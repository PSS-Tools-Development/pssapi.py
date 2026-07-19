from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import EngagementRaw as _EngagementRaw


class Engagement(_EngagementRaw, _EntityWithIdBase):
    def __init__(self, engagement_info: _EntityInfo) -> None:
        super().__init__(engagement_info)
        self._engagement_approval_state_enum: _enums.EngagementApprovalState = _parse.pss_str_enum(self.engagement_approval_state, _enums.EngagementApprovalState)
        self._engagement_group_user_state_enum: _enums.EngagementGroupUserState = _parse.pss_str_enum(self.engagement_group_user_state, _enums.EngagementGroupUserState)
        self._engagement_type_enum: _enums.EngagementType = _parse.pss_str_enum(self.engagement_type, _enums.EngagementType)
        self._outcome_type_enum: _enums.OutcomeType = _parse.pss_str_enum(self.outcome_type, _enums.OutcomeType)
        self._scoring_type_enum: _enums.EngagementScoringType = _parse.pss_str_enum(self.scoring_type, _enums.EngagementScoringType)

    @property
    def id(self) -> int:
        return self.engagement_id

    @property
    def engagement_approval_state_enum(self) -> _enums.EngagementApprovalState:
        return self._engagement_approval_state_enum

    @property
    def engagement_group_user_state_enum(self) -> _enums.EngagementGroupUserState:
        return self._engagement_group_user_state_enum

    @property
    def engagement_type_enum(self) -> _enums.EngagementType:
        return self._engagement_type_enum

    @property
    def outcome_type_enum(self) -> _enums.OutcomeType:
        return self._outcome_type_enum

    @property
    def scoring_type_enum(self) -> _enums.EngagementScoringType:
        return self._scoring_type_enum
