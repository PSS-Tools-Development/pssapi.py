
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AllianceRaw as _AllianceRaw
from ..types import EntityInfo as _EntityInfo


class Alliance(_EntityWithIdBase, _AllianceRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<Alliance {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<Alliance {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.alliance_id
