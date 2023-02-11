from datetime import timedelta as _timedelta
import json as _json
from typing import Any as _Any
from typing import Dict as _Dict
from typing import Tuple as _Tuple

from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ItemRaw as _ItemRaw
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse


class Item(_EntityWithIdBase, _ItemRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)


    def __repr__(self) -> str:
        return f'<Item {self.id}>'

    def __str__(self) -> str:
        return f'<Item {self.id}>'


    @property
    def id(self) -> int:
        return self.item_id
