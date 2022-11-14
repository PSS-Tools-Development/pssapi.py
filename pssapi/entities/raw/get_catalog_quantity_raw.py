"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class GetCatalogQuantityRaw:
    XML_NODE_NAME: str = 'GetCatalogQuantity'

    def __init__(self, get_catalog_quantity_info: _EntityInfo) -> None:
        self.limited_catalog_quantity: int = _parse.pss_int(get_catalog_quantity_info.get('LimitedCatalogQuantity'))
