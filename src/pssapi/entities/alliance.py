from .entity_base import EntityWithIdBase
from .raw import AllianceRaw


class Alliance(AllianceRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.alliance_id


__all__ = [
    "Alliance",
]
