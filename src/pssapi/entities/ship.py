from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ShipRaw as _ShipRaw


class Ship(_ShipRaw, _EntityWithIdBase):
    def __init__(self, ship_info: _EntityInfo) -> None:
        super().__init__(ship_info)
        self._ship_status_enum: _enums.ShipStatus = _parse.pss_str(self.ship_status, _enums.ShipStatus)

    @property
    def id(self) -> int:
        return self.ship_id

    @property
    def ship_status_enum(self) -> "_enums.ShipStatus":
        return self._ship_status_enum
