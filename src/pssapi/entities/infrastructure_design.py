from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import InfrastructureDesignRaw as _InfrastructureDesignRaw


class InfrastructureDesign(_InfrastructureDesignRaw, _EntityWithIdBase):
    def __init__(self, infrastructure_design_info: _EntityInfo) -> None:
        super().__init__(infrastructure_design_info)

    @property
    def id(self) -> int:
        return self.infrastructure_design_id
