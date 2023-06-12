from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ShipDesignRaw as _ShipDesignRaw


class ShipDesign(_ShipDesignRaw, _EntityWithIdBase):
    def __init__(self, ship_design_info: _EntityInfo) -> None:
        super().__init__(ship_design_info)
        self._ship_type_enum: _enums.ShipType = _parse.pss_str_enum(self.ship_type, _enums.ShipType)
        self._visibility_flags_enum: _enums.VisibilityFlags = _parse.pss_str_enum(self.visibility_flags, _enums.VisibilityFlags)

    @property
    def id(self) -> int:
        return self.ship_design_id

    @property
    def ship_type_enum(self) -> "_enums.ShipType":
        return self._ship_type_enum

    @property
    def visibility_flags_enum(self) -> "_enums.VisibilityFlags":
        return self._visibility_flags_enum
