from .entity_base import EntityBase
from .raw import GetCatalogQuantityRaw


class GetCatalogQuantity(GetCatalogQuantityRaw, EntityBase):
    pass


__all__ = [
    "GetCatalogQuantity",
]
