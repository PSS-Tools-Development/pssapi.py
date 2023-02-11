from datetime import timedelta as _timedelta
import json as _json
from typing import Any as _Any
from typing import Dict as _Dict
from typing import Tuple as _Tuple

from .entity_base import EntityBase as _EntityBase
from .raw import UserLoginRaw as _UserLoginRaw
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse


class UserLogin(_EntityBase, _UserLoginRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)


    def __repr__(self) -> str:
        return '<UserLogin>'

    def __str__(self) -> str:
        return '<UserLogin>'


