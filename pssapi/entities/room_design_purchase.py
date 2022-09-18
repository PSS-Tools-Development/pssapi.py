
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RoomDesignPurchaseRaw as _RoomDesignPurchaseRaw
from ..types import EntityInfo as _EntityInfo


class RoomDesignPurchase(_EntityWithIdBase, _RoomDesignPurchaseRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<RoomDesignPurchase {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<RoomDesignPurchase {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.room_design_purchase_id
