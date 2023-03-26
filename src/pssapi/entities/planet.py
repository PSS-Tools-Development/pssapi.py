from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import PlanetRaw as _PlanetRaw


class Planet(_PlanetRaw, _EntityBase):
    def __init__(self, planet_info: _EntityInfo) -> None:
        super().__init__(planet_info)
