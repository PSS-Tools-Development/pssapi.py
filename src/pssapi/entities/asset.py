from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AssetRaw as _AssetRaw


class Asset(_AssetRaw, _EntityWithIdBase):
    def __init__(self, asset_info: _EntityInfo) -> None:
        super().__init__(asset_info)
        self._asset_type_enum: _enums.AssetType = _parse.pss_str_enum(self.asset_type, _enums.AssetType)
        self._download_type_enum: _enums.DownloadType = _parse.pss_str_enum(self.download_type, _enums.DownloadType)

    @property
    def id(self) -> int:
        return self.asset_id

    @property
    def asset_type_enum(self) -> "_enums.AssetType":
        return self._asset_type_enum

    @property
    def download_type_enum(self) -> "_enums.DownloadType":
        return self._download_type_enum
