from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import StarSystemInfrastructuresRaw as _StarSystemInfrastructuresRaw


class StarSystemInfrastructures(_StarSystemInfrastructuresRaw, _EntityBase):
    def __init__(self, star_system_infrastructures_info: _EntityInfo) -> None:
        super().__init__(star_system_infrastructures_info)
