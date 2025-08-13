from .entity_base import EntityWithIdBase
from .raw import DrawDesignRaw


class DrawDesign(DrawDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.draw_design_id


__all__ = [
    "DrawDesign",
]
