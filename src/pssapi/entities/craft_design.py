from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CraftDesignRaw as _CraftDesignRaw


class CraftDesign(_CraftDesignRaw, _EntityWithIdBase):
    def __init__(self, craft_design_info: _EntityInfo) -> None:
        super().__init__(craft_design_info)

    @property
    def id(self) -> int:
        return self.craft_design_id
