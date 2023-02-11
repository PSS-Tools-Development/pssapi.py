from datetime import timedelta as _timedelta
import json as _json
from typing import Any as _Any
from typing import Dict as _Dict
from typing import Tuple as _Tuple

from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AnimationRaw as _AnimationRaw
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse


class Animation(_EntityWithIdBase, _AnimationRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)


    def __repr__(self) -> str:
        return f'<Animation {self.id}>'

    def __str__(self) -> str:
        return f'<Animation {self.id}>'


    @property
    def id(self) -> int:
        return self.animation_id
