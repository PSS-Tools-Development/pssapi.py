
from .entity_base import EntityBase as _EntityBase
from .raw import UserLoginRaw as _UserLoginRaw
from ..types import EntityInfo as _EntityInfo


class UserLogin(_EntityBase, _UserLoginRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return '<UserLogin>'

    def __str__(self) -> str:
        return '<UserLogin>'
