"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class GetCatalogQuantityRaw(EntityBaseRaw, tag="GetCatalogQuantity"):
    XML_NODE_NAME: str = "GetCatalogQuantity"

    limited_catalog_quantity: Optional[int] = attr(name="LimitedCatalogQuantity", default=None)

    def _key(self):
        return (self.limited_catalog_quantity,)


__all__ = [
    "GetCatalogQuantityRaw",
]
