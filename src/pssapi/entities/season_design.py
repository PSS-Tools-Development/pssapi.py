from .entity_base import EntityWithIdBase
from .raw import SeasonDesignRaw


class SeasonDesign(SeasonDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.season_design_id


__all__ = [
    "SeasonDesign",
]
