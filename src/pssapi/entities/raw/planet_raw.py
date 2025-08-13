"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class PlanetRaw(EntityBaseRaw, tag="Planet"):
    XML_NODE_NAME: str = "Planet"

    def _key(self):
        return tuple()


__all__ = [
    "PlanetRaw",
]
