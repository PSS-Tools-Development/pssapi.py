from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import DivisionDesignRaw as _DivisionDesignRaw


class DivisionDesign(_DivisionDesignRaw, _EntityWithIdBase):
    def __init__(self, division_design_info: _EntityInfo) -> None:
        super().__init__(division_design_info)
        self._division_type_enum: _enums.DivisionType = _parse.pss_str_enum(self.division_type, _enums.DivisionType)

    @property
    def id(self) -> int:
        return self.division_design_id

    @property
    def division_type_enum(self) -> "_enums.DivisionType":
        return self._division_type_enum
