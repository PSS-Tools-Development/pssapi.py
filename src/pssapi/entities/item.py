from .entity_base import EntityWithIdBase
from .raw import ItemRaw


class Item(ItemRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.item_id


__all__ = [
    "Item",
]
