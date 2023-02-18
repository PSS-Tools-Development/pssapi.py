
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RewardDesignRaw as _RewardDesignRaw
from ..types import EntityInfo as _EntityInfo


class RewardDesign(_EntityWithIdBase, _RewardDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<RewardDesign {self.id}>'

    def __str__(self) -> str:
        return f'<RewardDesign {self.id}>'

    @property
    def id(self) -> int:
        return self.reward_design_id
