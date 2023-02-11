from datetime import timedelta as _timedelta
import json as _json
from typing import Any as _Any
from typing import Dict as _Dict
from typing import Tuple as _Tuple

from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ShipDesignRaw as _ShipDesignRaw
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse


class ShipDesign(_EntityWithIdBase, _ShipDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)


    def __repr__(self) -> str:
        return f'<ShipDesign {self.id}>'

    def __str__(self) -> str:
        return f'<ShipDesign {self.id}>'


    @property
    def id(self) -> int:
        return self.ship_design_id
