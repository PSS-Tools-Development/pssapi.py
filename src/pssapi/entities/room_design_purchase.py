from .entity_base import EntityWithIdBase
from .raw import RoomDesignPurchaseRaw


class RoomDesignPurchase(RoomDesignPurchaseRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.room_design_purchase_id


__all__ = [
    "RoomDesignPurchase",
]
