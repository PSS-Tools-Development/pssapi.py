from .entity_base import EntityBase
from .raw import PrestigeRaw


class Prestige(PrestigeRaw, EntityBase):
    pass


__all__ = [
    "Prestige",
]
