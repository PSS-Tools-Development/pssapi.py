
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import DivisionDesignRaw as _DivisionDesignRaw
from ..types import EntityInfo as _EntityInfo


class DivisionDesign(_DivisionDesignRaw, _EntityWithIdBase):
    def __init__(self, division_design_info: _EntityInfo) -> None:
        super().__init__(division_design_info)

    @property
    def id(self) -> int:
        return self.division_design_id
