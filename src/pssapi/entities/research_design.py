from .entity_base import EntityWithIdBase
from .raw import ResearchDesignRaw


class ResearchDesign(ResearchDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.research_design_id


__all__ = [
    "ResearchDesign",
]
