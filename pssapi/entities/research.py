
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ResearchRaw as _ResearchRaw
from ..types import EntityInfo as _EntityInfo


class Research(_EntityWithIdBase, _ResearchRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<Research {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<Research {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.research_id
