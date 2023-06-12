from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ResearchRaw as _ResearchRaw


class Research(_ResearchRaw, _EntityWithIdBase):
    def __init__(self, research_info: _EntityInfo) -> None:
        super().__init__(research_info)
        self._research_state_enum: _enums.ResearchState = _parse.pss_str(self.research_state, _enums.ResearchState)

    @property
    def id(self) -> int:
        return self.research_id

    @property
    def research_state_enum(self) -> "_enums.ResearchState":
        return self._research_state_enum
