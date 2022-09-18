
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ConditionTypeRaw as _ConditionTypeRaw
from ..types import EntityInfo as _EntityInfo


class ConditionType(_EntityWithIdBase, _ConditionTypeRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<ConditionType {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<ConditionType {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.condition_type_id
