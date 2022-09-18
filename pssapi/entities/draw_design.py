
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import DrawDesignRaw as _DrawDesignRaw
from ..types import EntityInfo as _EntityInfo


class DrawDesign(_EntityWithIdBase, _DrawDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<DrawDesign {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<DrawDesign {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.draw_design_id
