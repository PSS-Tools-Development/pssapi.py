from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import DrawDesignRaw as _DrawDesignRaw


class DrawDesign(_DrawDesignRaw, _EntityWithIdBase):
    def __init__(self, draw_design_info: _EntityInfo) -> None:
        super().__init__(draw_design_info)

    @property
    def id(self) -> int:
        return self.draw_design_id
