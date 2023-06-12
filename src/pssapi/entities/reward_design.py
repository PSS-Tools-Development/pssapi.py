from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import RewardDesignMetadata as _RewardDesignMetadata
from .raw import RewardDesignRaw as _RewardDesignRaw


class RewardDesign(_RewardDesignRaw, _EntityWithIdBase):
    def __init__(self, reward_design_info: _EntityInfo) -> None:
        super().__init__(reward_design_info)
        self._reward_design_metadata: _RewardDesignMetadata = _RewardDesignMetadata(self.metadata)

    @property
    def id(self) -> int:
        return self.reward_design_id

    @property
    def reward_design_metadata(self) -> _RewardDesignMetadata:
        return self._reward_design_metadata
