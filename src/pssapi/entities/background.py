from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import BackgroundRaw as _BackgroundRaw


class Background(_BackgroundRaw, _EntityWithIdBase):
    def __init__(self, background_info: _EntityInfo) -> None:
        super().__init__(background_info)
        self._background_effect_type_enum: _enums.BackgroundEffectType = _parse.pss_str_enum(self.background_effect_type, _enums.BackgroundEffectType)
        self._background_type_enum: _enums.BackgroundType = _parse.pss_str_enum(self.background_type, _enums.BackgroundType)
        self._environment_type_enum: _enums.EnvironmentType = _parse.pss_str_enum(self.environment_type, _enums.EnvironmentType)
        self._hazard_category_enum: _enums.HazardCategory = _parse.pss_str_enum(self.hazard_category, _enums.HazardCategory)
        self._hazard_type_enum: _enums.HazardType = _parse.pss_str_enum(self.hazard_type, _enums.HazardType)
        self._orbit_anchor_alignment_enum: _enums.OrbitAnchorAlignment = _parse.pss_str_enum(self.orbit_anchor_alignment, _enums.OrbitAnchorAlignment)

    @property
    def id(self) -> int:
        return self.background_id

    @property
    def background_effect_type_enum(self) -> "_enums.BackgroundEffectType":
        return self._background_effect_type_enum

    @property
    def background_type_enum(self) -> "_enums.BackgroundType":
        return self._background_type_enum

    @property
    def environment_type_enum(self) -> "_enums.EnvironmentType":
        return self._environment_type_enum

    @property
    def hazard_category_enum(self) -> "_enums.HazardCategory":
        return self._hazard_category_enum

    @property
    def hazard_type_enum(self) -> "_enums.HazardType":
        return self._hazard_type_enum

    @property
    def orbit_anchor_alignment_enum(self) -> "_enums.OrbitAnchorAlignment":
        return self._orbit_anchor_alignment_enum
