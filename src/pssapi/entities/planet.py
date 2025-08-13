from .entity_base import EntityBase
from .raw import PlanetRaw


class Planet(PlanetRaw, EntityBase):
    pass


__all__ = [
    "Planet",
]
