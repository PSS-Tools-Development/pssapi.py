from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import MissileDesignMetadata as _MissileDesignMetadata
from .raw import MissileDesignRaw as _MissileDesignRaw


class MissileDesign(_MissileDesignRaw, _EntityWithIdBase):
    def __init__(self, missile_design_info: _EntityInfo) -> None:
        super().__init__(missile_design_info)
        self._explosion_type_enum: _enums.ExplosionType = _parse.pss_str_enum(self.explosion_type, _enums.ExplosionType)
        self._flight_type_enum: _enums.FlightType = _parse.pss_str_enum(self.flight_type, _enums.FlightType)
        self._missile_design_metadata: _MissileDesignMetadata = _MissileDesignMetadata(self.metadata)
        self._missile_type_enum: _enums.MissileType = _parse.pss_str_enum(self.missile_type, _enums.MissileType)

    @property
    def id(self) -> int:
        return self.missile_design_id

    @property
    def explosion_type_enum(self) -> "_enums.ExplosionType":
        return self._explosion_type_enum

    @property
    def flight_type_enum(self) -> "_enums.FlightType":
        return self._flight_type_enum

    @property
    def missile_design_metadata(self) -> _MissileDesignMetadata:
        return self._missile_design_metadata

    @property
    def missile_type_enum(self) -> "_enums.MissileType":
        return self._missile_type_enum
