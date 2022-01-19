from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RoomDesignPurchaseRaw as _RoomDesignPurchaseRaw


class RoomDesignPurchase(_RoomDesignPurchaseRaw, _EntityWithIdBase):
    def __init__(self, room_design_purchase_info: _EntityInfo) -> None:
        super().__init__(room_design_purchase_info)

    @property
    def id(self) -> int:
        return self.room_design_purchase_id
