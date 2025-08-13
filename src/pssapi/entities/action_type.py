from .entity_base import EntityWithIdBase
from .raw import ActionTypeRaw


class ActionType(ActionTypeRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.action_type_id


__all__ = [
    "ActionType",
]
