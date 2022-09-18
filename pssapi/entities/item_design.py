
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ItemDesignRaw as _ItemDesignRaw
from ..types import EntityInfo as _EntityInfo


class ItemDesign(_EntityWithIdBase, _ItemDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<ItemDesign {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<ItemDesign {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.item_design_id
