from datetime import timedelta as _timedelta
import json as _json
from typing import Any as _Any
from typing import Dict as _Dict
from typing import Tuple as _Tuple

from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import RoomDesignPurchaseRaw as _RoomDesignPurchaseRaw
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse


class RoomDesignPurchase(_EntityWithIdBase, _RoomDesignPurchaseRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)


    def __repr__(self) -> str:
        return f'<RoomDesignPurchase {self.id}>'

    def __str__(self) -> str:
        return f'<RoomDesignPurchase {self.id}>'


    @property
    def id(self) -> int:
        return self.room_design_purchase_id
