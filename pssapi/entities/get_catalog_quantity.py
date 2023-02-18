
from .entity_base import EntityBase as _EntityBase
from .raw import GetCatalogQuantityRaw as _GetCatalogQuantityRaw
from ..types import EntityInfo as _EntityInfo


class GetCatalogQuantity(_EntityBase, _GetCatalogQuantityRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return '<GetCatalogQuantity>'

    def __str__(self) -> str:
        return '<GetCatalogQuantity>'
