from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AllianceRaw as _AllianceRaw


class Alliance(_AllianceRaw, _EntityWithIdBase):
    def __init__(self, alliance_info: _EntityInfo) -> None:
        super().__init__(alliance_info)

    @property
    def id(self) -> int:
        return self.alliance_id
