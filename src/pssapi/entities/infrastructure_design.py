from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import InfrastructureDesignRaw as _InfrastructureDesignRaw


class InfrastructureDesign(_InfrastructureDesignRaw, _EntityWithIdBase):
    def __init__(self, infrastructure_design_info: _EntityInfo) -> None:
        super().__init__(infrastructure_design_info)
        self._infrastructure_reward_type_enum: _enums.InfrastructureRewardType = _parse.pss_str_enum(self.infrastructure_reward_type, _enums.InfrastructureRewardType)
        self._infrastructure_type_enum: _enums.InfrastructureType = _parse.pss_str_enum(self.infrastructure_type, _enums.InfrastructureType)

    @property
    def id(self) -> int:
        return self.infrastructure_design_id

    @property
    def infrastructure_reward_type_enum(self) -> _enums.InfrastructureRewardType:
        return self._infrastructure_reward_type_enum

    @property
    def infrastructure_type_enum(self) -> _enums.InfrastructureType:
        return self._infrastructure_type_enum
