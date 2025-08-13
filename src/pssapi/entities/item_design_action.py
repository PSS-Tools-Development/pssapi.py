from .entity_base import EntityWithIdBase
from .raw import ItemDesignActionRaw


class ItemDesignAction(ItemDesignActionRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.item_design_action_id


__all__ = [
    "ItemDesignAction",
]
