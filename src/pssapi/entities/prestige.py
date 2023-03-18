from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import PrestigeRaw as _PrestigeRaw


class Prestige(_PrestigeRaw, _EntityBase):
    def __init__(self, prestige_info: _EntityInfo) -> None:
        super().__init__(prestige_info)
