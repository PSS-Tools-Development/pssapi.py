from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import GetCatalogQuantityRaw as _GetCatalogQuantityRaw


class GetCatalogQuantity(_GetCatalogQuantityRaw, _EntityBase):
    def __init__(self, get_catalog_quantity_info: _EntityInfo) -> None:
        super().__init__(get_catalog_quantity_info)
