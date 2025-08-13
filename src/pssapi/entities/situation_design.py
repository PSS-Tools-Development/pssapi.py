from .entity_base import EntityWithIdBase
from .raw import SituationDesignRaw


class SituationDesign(SituationDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.situation_design_id


__all__ = [
    "SituationDesign",
]
