from .entity_base import EntityWithIdBase
from .raw import MissionDesignRaw


class MissionDesign(MissionDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.mission_design_id


__all__ = [
    "MissionDesign",
]
