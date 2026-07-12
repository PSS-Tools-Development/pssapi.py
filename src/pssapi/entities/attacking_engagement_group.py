from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import AttackingEngagementGroupRaw as _AttackingEngagementGroupRaw


class AttackingEngagementGroup(_AttackingEngagementGroupRaw, _EntityBase):
    def __init__(self, attacking_engagement_group_info: _EntityInfo) -> None:
        super().__init__(attacking_engagement_group_info)
