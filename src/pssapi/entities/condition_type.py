from .entity_base import EntityWithIdBase
from .raw import ConditionTypeRaw


class ConditionType(ConditionTypeRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.condition_type_id


__all__ = [
    "ConditionType",
]
