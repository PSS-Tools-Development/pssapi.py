
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ShipRaw as _ShipRaw
from ..types import EntityInfo as _EntityInfo


class Ship(_EntityWithIdBase, _ShipRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<Ship {self.id}>'

    def __str__(self) -> str:
        return f'<Ship {self.id}>'

    @property
    def id(self) -> int:
        return self.ship_id
