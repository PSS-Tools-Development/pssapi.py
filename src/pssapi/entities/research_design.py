from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ResearchDesignRaw as _ResearchDesignRaw


class ResearchDesign(_ResearchDesignRaw, _EntityWithIdBase):
    def __init__(self, research_design_info: _EntityInfo) -> None:
        super().__init__(research_design_info)

    @property
    def id(self) -> int:
        return self.research_design_id
