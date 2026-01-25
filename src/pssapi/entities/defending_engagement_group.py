from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import DefendingEngagementGroupRaw as _DefendingEngagementGroupRaw


class DefendingEngagementGroup(_DefendingEngagementGroupRaw, _EntityBase):
    def __init__(self, defending_engagement_group_info: _EntityInfo) -> None:
        super().__init__(defending_engagement_group_info)
