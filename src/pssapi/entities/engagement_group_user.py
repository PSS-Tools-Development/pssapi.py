from typing import List as _List

from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import EngagementGroupUserRaw as _EngagementGroupUserRaw


class EngagementGroupUser(_EngagementGroupUserRaw, _EntityWithIdBase):
    def __init__(self, engagement_group_user_info: _EntityInfo) -> None:
        super().__init__(engagement_group_user_info)
        self._approval_state_enum: _enums.EngagementApprovalState = _parse.pss_str_enum(self.approval_state, _enums.EngagementApprovalState)
        self._engagement_group_user_state_enum: _enums.EngagementGroupUserState = _parse.pss_str_enum(self.engagement_group_user_state, _enums.EngagementGroupUserState)
        self._user_type_enum: _enums.UserType = _parse.pss_str_enum(self.user_type, _enums.UserType)
        self._attacked_engagement_group_user_ids_list: _List[int] = [int(x) for x in _parse.pss_str_list(self.attacked_engagement_group_user_ids)]

    @property
    def id(self) -> int:
        return self.engagement_group_user_id

    @property
    def approval_state_enum(self) -> _enums.EngagementApprovalState:
        return self._approval_state_enum

    @property
    def engagement_group_user_state_enum(self) -> _enums.EngagementGroupUserState:
        return self._engagement_group_user_state_enum

    @property
    def user_type_enum(self) -> _enums.UserType:
        return self._user_type_enum

    @property
    def attacked_engagement_group_user_ids_list(self) -> _List[int]:
        return self._attacked_engagement_group_user_ids_list
