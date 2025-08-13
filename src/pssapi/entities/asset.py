from .entity_base import EntityWithIdBase
from .raw import AssetRaw


class Asset(AssetRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.asset_id


__all__ = [
    "Asset",
]
