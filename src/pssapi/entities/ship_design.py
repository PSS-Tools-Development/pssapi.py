from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ShipDesignRaw as _ShipDesignRaw


class ShipDesign(_ShipDesignRaw, _EntityWithIdBase):
    def __init__(self, ship_design_info: _EntityInfo) -> None:
        super().__init__(ship_design_info)

    @property
    def id(self) -> int:
        return self.ship_design_id
