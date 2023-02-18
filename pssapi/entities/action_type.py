
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ActionTypeRaw as _ActionTypeRaw
from ..types import EntityInfo as _EntityInfo


class ActionType(_EntityWithIdBase, _ActionTypeRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<ActionType {self.id}>'

    def __str__(self) -> str:
        return f'<ActionType {self.id}>'

    @property
    def id(self) -> int:
        return self.action_type_id
