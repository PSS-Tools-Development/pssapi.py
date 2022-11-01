
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import DivisionDesignRaw as _DivisionDesignRaw
from ..types import EntityInfo as _EntityInfo


class DivisionDesign(_EntityWithIdBase, _DivisionDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<DivisionDesign {self.id}>'

    def __str__(self) -> str:
        return f'<DivisionDesign {self.id}>'

    @property
    def id(self) -> int:
        return self.division_design_id
