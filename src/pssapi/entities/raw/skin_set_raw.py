"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as EntityBaseRaw


class SkinSetRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "SkinSet"

    def __init__(self, skin_set_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._approval_flags: str = _parse.pss_str(skin_set_info.pop("ApprovalFlags", None))
        self._cost_string: str = _parse.pss_str(skin_set_info.pop("CostString", None))
        self._date_updated: _datetime = _parse.pss_datetime(skin_set_info.pop("DateUpdated", None))
        self._flags: int = _parse.pss_int(skin_set_info.pop("Flags", None))
        self._metadata: str = _parse.pss_str(skin_set_info.pop("Metadata", None))
        self._requirement_string: str = _parse.pss_str(skin_set_info.pop("RequirementString", None))
        self._skin_set_description: str = _parse.pss_str(skin_set_info.pop("SkinSetDescription", None))
        self._skin_set_id: int = _parse.pss_int(skin_set_info.pop("SkinSetId", None))
        self._skin_set_name: str = _parse.pss_str(skin_set_info.pop("SkinSetName", None))
        self._sprite_id: int = _parse.pss_int(skin_set_info.pop("SpriteId", None))
        super().__init__(skin_set_info)

    @property
    def approval_flags(self) -> str:
        return self._approval_flags

    @property
    def cost_string(self) -> str:
        return self._cost_string

    @property
    def date_updated(self) -> _datetime:
        return self._date_updated

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def skin_set_description(self) -> str:
        return self._skin_set_description

    @property
    def skin_set_id(self) -> int:
        return self._skin_set_id

    @property
    def skin_set_name(self) -> str:
        return self._skin_set_name

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    def _key(self):
        return (
            self.approval_flags,
            self.cost_string,
            self.date_updated,
            self.flags,
            self.metadata,
            self.requirement_string,
            self.skin_set_description,
            self.skin_set_id,
            self.skin_set_name,
            self.sprite_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ApprovalFlags": self.approval_flags,
                "CostString": self.cost_string,
                "DateUpdated": self.date_updated,
                "Flags": self.flags,
                "Metadata": self.metadata,
                "RequirementString": self.requirement_string,
                "SkinSetDescription": self.skin_set_description,
                "SkinSetId": self.skin_set_id,
                "SkinSetName": self.skin_set_name,
                "SpriteId": self.sprite_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
