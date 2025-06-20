"""
This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class AssetRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Asset"

    def __init__(self, asset_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._asset_design_name: str = _parse.pss_str(asset_info.pop("AssetDesignName", None))
        self._asset_id: int = _parse.pss_int(asset_info.pop("AssetId", None))
        self._asset_label: str = _parse.pss_str(asset_info.pop("AssetLabel", None))
        self._asset_type: str = _parse.pss_str(asset_info.pop("AssetType", None))
        self._download_type: str = _parse.pss_str(asset_info.pop("DownloadType", None))
        self._file_id: int = _parse.pss_int(asset_info.pop("FileId", None))
        super().__init__(asset_info)

    @property
    def asset_design_name(self) -> str:
        return self._asset_design_name

    @property
    def asset_id(self) -> int:
        return self._asset_id

    @property
    def asset_label(self) -> str:
        return self._asset_label

    @property
    def asset_type(self) -> str:
        return self._asset_type

    @property
    def download_type(self) -> str:
        return self._download_type

    @property
    def file_id(self) -> int:
        return self._file_id

    def _key(self):
        return (
            self.asset_design_name,
            self.asset_id,
            self.asset_label,
            self.asset_type,
            self.download_type,
            self.file_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AssetDesignName": self.asset_design_name,
                "AssetId": self.asset_id,
                "AssetLabel": self.asset_label,
                "AssetType": self.asset_type,
                "DownloadType": self.download_type,
                "FileId": self.file_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
