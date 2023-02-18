
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SaleRaw as _SaleRaw
from ..types import EntityInfo as _EntityInfo


class Sale(_EntityWithIdBase, _SaleRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<Sale {self.id}>'

    def __str__(self) -> str:
        return f'<Sale {self.id}>'

    @property
    def id(self) -> int:
        return self.sale_id
