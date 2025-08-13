from .entity_base import EntityWithIdBase
from .raw import MissileDesignRaw


class MissileDesign(MissileDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.missile_design_id


__all__ = [
    "MissileDesign",
]
