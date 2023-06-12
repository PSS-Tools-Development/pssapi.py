from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import LiveOpsRaw as _LiveOpsRaw


class LiveOps(_LiveOpsRaw, _EntityWithIdBase):
    def __init__(self, live_ops_info: _EntityInfo) -> None:
        super().__init__(live_ops_info)
        self._daily_reward_type_enum: _enums.DailyRewardType = _parse.pss_str_enum(self.daily_reward_type, _enums.DailyRewardType)
        self._limited_catalog_currency_type_enum: _enums.CurrencyType = _parse.pss_str_enum(self.limited_catalog_currency_type, _enums.CurrencyType)
        self._limited_catalog_type_enum: _enums.SaleType = _parse.pss_str_enum(self.limited_catalog_type, _enums.SaleType)
        self._sale_item_mask_enum: _enums.SaleItemMask = _parse.pss_int_flag(self.sale_item_mask, _enums.SaleItemMask)
        self._sale_type_enum: _enums.SaleType = _parse.pss_str_enum(self.sale_type, _enums.SaleType)

    @property
    def id(self) -> int:
        return self.live_ops_id

    @property
    def daily_reward_type_enum(self) -> "_enums.DailyRewardType":
        return self._daily_reward_type_enum

    @property
    def limited_catalog_currency_type_enum(self) -> "_enums.CurrencyType":
        return self._limited_catalog_currency_type_enum

    @property
    def limited_catalog_type_enum(self) -> "_enums.SaleType":
        return self._limited_catalog_type_enum

    @property
    def sale_item_mask_enum(self) -> "_enums.SaleItemMask":
        return self._sale_item_mask_enum

    @property
    def sale_type_enum(self) -> "_enums.SaleType":
        return self._sale_type_enum
