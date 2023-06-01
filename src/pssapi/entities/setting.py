from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SettingRaw as _SettingRaw


class Setting(_SettingRaw, _EntityWithIdBase):
    def __init__(self, setting_info: _EntityInfo) -> None:
        super().__init__(setting_info)
        self._a_feature_mask_enum: _enums.FeatureFlag = _parse.pss_int(self.a_feature_mask, _enums.FeatureFlag)
        self._b_feature_mask_enum: _enums.FeatureFlag = _parse.pss_int(self.b_feature_mask, _enums.FeatureFlag)
        self._checksum_type_enum: _enums.ChecksumType = _parse.pss_str(self.checksum_type, _enums.ChecksumType)
        self._daily_reward_type_enum: _enums.DailyRewardType = _parse.pss_str(self.daily_reward_type, _enums.DailyRewardType)
        self._feature_mask_enum: _enums.FeatureFlag = _parse.pss_int(self.feature_mask, _enums.FeatureFlag)
        self._flags_enum: _enums.SettingFlags = _parse.pss_int(self.flags, _enums.SettingFlags)
        self._limited_catalog_currency_type_enum: _enums.CurrencyType = _parse.pss_str(self.limited_catalog_currency_type, _enums.CurrencyType)
        self._limited_catalog_type_enum: _enums.SaleType = _parse.pss_str(self.limited_catalog_type, _enums.SaleType)
        self._production_server_enum: _enums.ProductionServer = _parse.pss_str(self.production_server, _enums.ProductionServer)
        self._sale_item_mask_enum: _enums.SaleItemMask = _parse.pss_int(self.sale_item_mask, _enums.SaleItemMask)
        self._sale_type_enum: _enums.SaleType = _parse.pss_str(self.sale_type, _enums.SaleType)

    @property
    def id(self) -> int:
        return self.setting_id

    @property
    def a_feature_mask_enum(self) -> "_enums.FeatureFlag":
        return self._a_feature_mask_enum

    @property
    def b_feature_mask_enum(self) -> "_enums.FeatureFlag":
        return self._b_feature_mask_enum

    @property
    def checksum_type_enum(self) -> "_enums.ChecksumType":
        return self._checksum_type_enum

    @property
    def daily_reward_type_enum(self) -> "_enums.DailyRewardType":
        return self._daily_reward_type_enum

    @property
    def feature_mask_enum(self) -> "_enums.FeatureFlag":
        return self._feature_mask_enum

    @property
    def flags_enum(self) -> "_enums.SettingFlags":
        return self._flags_enum

    @property
    def limited_catalog_currency_type_enum(self) -> "_enums.CurrencyType":
        return self._limited_catalog_currency_type_enum

    @property
    def limited_catalog_type_enum(self) -> "_enums.SaleType":
        return self._limited_catalog_type_enum

    @property
    def production_server_enum(self) -> "_enums.ProductionServer":
        return self._production_server_enum

    @property
    def sale_item_mask_enum(self) -> "_enums.SaleItemMask":
        return self._sale_item_mask_enum

    @property
    def sale_type_enum(self) -> "_enums.SaleType":
        return self._sale_type_enum
