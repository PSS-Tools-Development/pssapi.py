"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class GetCatalogQuantityRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "GetCatalogQuantity"

    def __init__(self, get_catalog_quantity_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._limited_catalog_quantity: int = _parse.pss_int(get_catalog_quantity_info.pop("LimitedCatalogQuantity", None))
        super().__init__(get_catalog_quantity_info)

    @property
    def limited_catalog_quantity(self) -> int:
        return self._limited_catalog_quantity

    def _key(self):
        return (self.limited_catalog_quantity,)

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "LimitedCatalogQuantity": self.limited_catalog_quantity,
            }
            self._dict.update(super().__dict__())

        return self._dict
