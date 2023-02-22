
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ResearchRaw as _ResearchRaw
from ..types import EntityInfo as _EntityInfo


class Research(_ResearchRaw, _EntityWithIdBase):
    def __init__(self, research_info: _EntityInfo) -> None:
        super().__init__(research_info)

    @property
    def id(self) -> int:
        return self.research_id
