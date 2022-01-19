from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ActionTypeRaw as _ActionTypeRaw


class ActionType(_ActionTypeRaw, _EntityWithIdBase):
    def __init__(self, action_type_info: _EntityInfo) -> None:
        super().__init__(action_type_info)

    @property
    def id(self) -> int:
        return self.action_type_id
