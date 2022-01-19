from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ShipRaw as _ShipRaw


class Ship(_ShipRaw, _EntityWithIdBase):
    def __init__(self, ship_info: _EntityInfo) -> None:
        super().__init__(ship_info)

    @property
    def id(self) -> int:
        return self.ship_id
