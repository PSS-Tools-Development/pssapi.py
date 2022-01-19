from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ItemRaw as _ItemRaw


class Item(_ItemRaw, _EntityWithIdBase):
    def __init__(self, item_info: _EntityInfo) -> None:
        super().__init__(item_info)

    @property
    def id(self) -> int:
        return self.item_id
