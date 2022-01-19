from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ConditionTypeRaw as _ConditionTypeRaw


class ConditionType(_ConditionTypeRaw, _EntityWithIdBase):
    def __init__(self, condition_type_info: _EntityInfo) -> None:
        super().__init__(condition_type_info)

    @property
    def id(self) -> int:
        return self.condition_type_id
