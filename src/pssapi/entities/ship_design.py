from .entity_base import EntityWithIdBase
from .raw import ShipDesignRaw


class ShipDesign(ShipDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.ship_design_id


__all__ = [
    "ShipDesign",
]
