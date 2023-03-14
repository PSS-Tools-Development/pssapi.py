from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RewardDesignRaw as _RewardDesignRaw


class RewardDesign(_RewardDesignRaw, _EntityWithIdBase):
    def __init__(self, reward_design_info: _EntityInfo) -> None:
        super().__init__(reward_design_info)

    @property
    def id(self) -> int:
        return self.reward_design_id
