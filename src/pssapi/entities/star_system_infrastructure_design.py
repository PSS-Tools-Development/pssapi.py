from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import StarSystemInfrastructureDesignRaw as _StarSystemInfrastructureDesignRaw


class StarSystemInfrastructureDesign(_StarSystemInfrastructureDesignRaw, _EntityWithIdBase):
    def __init__(self, star_system_infrastructure_design_info: _EntityInfo) -> None:
        super().__init__(star_system_infrastructure_design_info)

    @property
    def id(self) -> int:
        return self.star_system_infrastructure_design_id
