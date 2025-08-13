from .entity_base import EntityWithIdBase
from .raw import ResearchRaw


class Research(ResearchRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.research_id


__all__ = [
    "Research",
]
