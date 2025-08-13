from .entity_base import EntityWithIdBase
from .raw import ItemDesignRaw


class ItemDesign(ItemDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.item_design_id


__all__ = [
    "ItemDesign",
]
