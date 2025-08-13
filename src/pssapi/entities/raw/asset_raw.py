"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class AssetRaw(EntityBaseRaw, tag="Asset"):
    XML_NODE_NAME: str = "Asset"

    asset_design_name: Optional[str] = attr(name="AssetDesignName", default=None)
    asset_id: Optional[int] = attr(name="AssetId", default=None)
    asset_label: Optional[str] = attr(name="AssetLabel", default=None)
    asset_type: Optional[str] = attr(name="AssetType", default=None)
    download_type: Optional[str] = attr(name="DownloadType", default=None)
    file_id: Optional[int] = attr(name="FileId", default=None)

    def _key(self):
        return (
            self.asset_design_name,
            self.asset_id,
            self.asset_label,
            self.asset_type,
            self.download_type,
            self.file_id,
        )


__all__ = [
    "AssetRaw",
]
