from .entity_base import EntityWithIdBase
from .raw import SaleRaw


class Sale(SaleRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.sale_id


__all__ = [
    "Sale",
]
