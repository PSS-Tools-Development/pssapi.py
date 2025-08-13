from .entity_base import EntityWithIdBase
from .raw import ShipRaw


class Ship(ShipRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.ship_id


__all__ = [
    "Ship",
]
