from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ResearchDesignRaw as _ResearchDesignRaw


class ResearchDesign(_ResearchDesignRaw, _EntityWithIdBase):
    def __init__(self, research_design_info: _EntityInfo) -> None:
        super().__init__(research_design_info)
        self._availability_mask_enum: _enums.AvailabilityMask = _parse.pss_int_flag(self.availability_mask, _enums.AvailabilityMask)
        self._research_design_type_enum: _enums.ResearchDesignType = _parse.pss_str_enum(self.research_design_type, _enums.ResearchDesignType)
        self._visibility_flags_enum: _enums.VisibilityFlags = _parse.pss_str_enum(self.visibility_flags, _enums.VisibilityFlags)

    @property
    def id(self) -> int:
        return self.research_design_id

    @property
    def availability_mask_enum(self) -> "_enums.AvailabilityMask":
        return self._availability_mask_enum

    @property
    def research_design_type_enum(self) -> "_enums.ResearchDesignType":
        return self._research_design_type_enum

    @property
    def visibility_flags_enum(self) -> "_enums.VisibilityFlags":
        return self._visibility_flags_enum
