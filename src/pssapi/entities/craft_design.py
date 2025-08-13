from .entity_base import EntityWithIdBase
from .raw import CraftDesignRaw


class CraftDesign(CraftDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.craft_design_id


__all__ = [
    "CraftDesign",
]
