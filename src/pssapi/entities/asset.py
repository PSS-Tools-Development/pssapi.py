from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AssetRaw as _AssetRaw


class Asset(_AssetRaw, _EntityWithIdBase):
    def __init__(self, asset_info: _EntityInfo) -> None:
        super().__init__(asset_info)

    @property
    def id(self) -> int:
        return self.asset_id
