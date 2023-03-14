from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SaleRaw as _SaleRaw


class Sale(_SaleRaw, _EntityWithIdBase):
    def __init__(self, sale_info: _EntityInfo) -> None:
        super().__init__(sale_info)

    @property
    def id(self) -> int:
        return self.sale_id
