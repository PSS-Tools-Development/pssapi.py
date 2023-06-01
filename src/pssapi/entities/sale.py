from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SaleRaw as _SaleRaw


class Sale(_SaleRaw, _EntityWithIdBase):
    def __init__(self, sale_info: _EntityInfo) -> None:
        super().__init__(sale_info)
        self._currency_type_enum: _enums.CurrencyType = _parse.pss_str_enum(self.currency_type, _enums.CurrencyType)
        self._sale_status_enum: _enums.SaleStatus = _parse.pss_str_enum(self.sale_status, _enums.SaleStatus)

    @property
    def id(self) -> int:
        return self.sale_id

    @property
    def currency_type_enum(self) -> "_enums.CurrencyType":
        return self._currency_type_enum

    @property
    def sale_status_enum(self) -> "_enums.SaleStatus":
        return self._sale_status_enum
