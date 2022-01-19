from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ItemDesignRaw as _ItemDesignRaw


class ItemDesign(_ItemDesignRaw, _EntityWithIdBase):
    def __init__(self, item_design_info: _EntityInfo) -> None:
        super().__init__(item_design_info)

    @property
    def id(self) -> int:
        return self.item_design_id
