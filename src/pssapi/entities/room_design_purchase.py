from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RoomDesignPurchaseRaw as _RoomDesignPurchaseRaw


class RoomDesignPurchase(_RoomDesignPurchaseRaw, _EntityWithIdBase):
    def __init__(self, room_design_purchase_info: _EntityInfo) -> None:
        super().__init__(room_design_purchase_info)
        self._availability_mask_enum: _enums.AvailabilityMask = _parse.pss_int_flag(self.availability_mask, _enums.AvailabilityMask)

    @property
    def id(self) -> int:
        return self.room_design_purchase_id

    @property
    def availability_mask_enum(self) -> "_enums.AvailabilityMask":
        return self._availability_mask_enum
