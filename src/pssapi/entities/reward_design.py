from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import RewardDesignMetadata as _RewardDesignMetadata
from .raw import RewardDesignRaw as _RewardDesignRaw


class RewardDesign(_RewardDesignRaw, _EntityWithIdBase):
    def __init__(self, reward_design_info: _EntityInfo) -> None:
        super().__init__(reward_design_info)
        self._flags_enum: _enums.UserStatus = _parse.pss_int_flag(self.flags, _enums.UserStatus)
        self._reward_type_enum: _enums.RewardType = _parse.pss_str_enum(self.reward_type, _enums.RewardType)
        self._reward_design_metadata: _RewardDesignMetadata = _RewardDesignMetadata(self.metadata)

    @property
    def id(self) -> int:
        return self.reward_design_id

    @property
    def flags_enum(self) -> "_enums.UserStatus":
        """
        Only UserStatus.PURCHASED_TOURNAMENT_BOX... values are usually used.
        """
        return self._flags_enum

    @property
    def reward_design_metadata(self) -> _RewardDesignMetadata:
        return self._reward_design_metadata

    @property
    def reward_type_enum(self) -> "_enums.RewardType":
        return self._reward_type_enum
