from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserSeasonRaw as _UserSeasonRaw


class UserSeason(_UserSeasonRaw, _EntityWithIdBase):
    def __init__(self, user_season_info: _EntityInfo) -> None:
        super().__init__(user_season_info)
        self._purchase_vip_status_enum: _enums.PurchaseVIPStatus = _parse.pss_str_enum(self.purchase_vip_status, _enums.PurchaseVIPStatus)

    @property
    def id(self) -> int:
        return self.user_season_id

    @property
    def purchase_vip_status_enum(self) -> "_enums.PurchaseVIPStatus":
        return self._purchase_vip_status_enum
