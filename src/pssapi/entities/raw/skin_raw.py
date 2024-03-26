"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw


class SkinRaw(EntityBaseRaw):
    XML_NODE_NAME: str = "Skin"

    def __init__(self, skin_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._animation_id: int = _parse.pss_int(skin_info.pop("AnimationId", None))
        self._approval_flags: str = _parse.pss_str(skin_info.pop("ApprovalFlags", None))
        self._date_updated: _datetime = _parse.pss_datetime(skin_info.pop("DateUpdated", None))
        self._flags: int = _parse.pss_int(skin_info.pop("Flags", None))
        self._metadata: str = _parse.pss_str(skin_info.pop("Metadata", None))
        self._original_animation_id: int = _parse.pss_int(skin_info.pop("OriginalAnimationId", None))
        self._original_sprite_id: int = _parse.pss_int(skin_info.pop("OriginalSpriteId", None))
        self._race_id: int = _parse.pss_int(skin_info.pop("RaceId", None))
        self._reference_id: int = _parse.pss_int(skin_info.pop("ReferenceId", None))
        self._requirement_string: str = _parse.pss_str(skin_info.pop("RequirementString", None))
        self._root_id: int = _parse.pss_int(skin_info.pop("RootId", None))
        self._skin_description: str = _parse.pss_str(skin_info.pop("SkinDescription", None))
        self._skin_id: int = _parse.pss_int(skin_info.pop("SkinId", None))
        self._skin_name: str = _parse.pss_str(skin_info.pop("SkinName", None))
        self._skin_set_id: int = _parse.pss_int(skin_info.pop("SkinSetId", None))
        self._skin_type: str = _parse.pss_str(skin_info.pop("SkinType", None))
        self._sprite_id: int = _parse.pss_int(skin_info.pop("SpriteId", None))
        self._sprite_type: str = _parse.pss_str(skin_info.pop("SpriteType", None))
        self._user_id: int = _parse.pss_int(skin_info.pop("UserId", None))
        super().__init__(skin_info)

    @property
    def animation_id(self) -> int:
        return self._animation_id

    @property
    def approval_flags(self) -> str:
        return self._approval_flags

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
    def original_animation_id(self) -> int:
        return self._original_animation_id

    @property
    def original_sprite_id(self) -> int:
        return self._original_sprite_id

    @property
    def race_id(self) -> int:
        return self._race_id

    @property
    def reference_id(self) -> int:
        return self._reference_id

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def root_id(self) -> int:
        return self._root_id

    @property
    def skin_description(self) -> str:
        return self._skin_description

    @property
    def skin_id(self) -> int:
        return self._skin_id

    @property
    def skin_name(self) -> str:
        return self._skin_name

    @property
    def skin_set_id(self) -> int:
        return self._skin_set_id

    @property
    def skin_type(self) -> str:
        return self._skin_type

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    @property
    def sprite_type(self) -> str:
        return self._sprite_type

    @property
    def user_id(self) -> int:
        return self._user_id

    def _key(self):
        return (
            self.animation_id,
            self.approval_flags,
            self.date_updated,
            self.flags,
            self.metadata,
            self.original_animation_id,
            self.original_sprite_id,
            self.race_id,
            self.reference_id,
            self.requirement_string,
            self.root_id,
            self.skin_description,
            self.skin_id,
            self.skin_name,
            self.skin_set_id,
            self.skin_type,
            self.sprite_id,
            self.sprite_type,
            self.user_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AnimationId": self.animation_id,
                "ApprovalFlags": self.approval_flags,
                "DateUpdated": self.date_updated,
                "Flags": self.flags,
                "Metadata": self.metadata,
                "OriginalAnimationId": self.original_animation_id,
                "OriginalSpriteId": self.original_sprite_id,
                "RaceId": self.race_id,
                "ReferenceId": self.reference_id,
                "RequirementString": self.requirement_string,
                "RootId": self.root_id,
                "SkinDescription": self.skin_description,
                "SkinId": self.skin_id,
                "SkinName": self.skin_name,
                "SkinSetId": self.skin_set_id,
                "SkinType": self.skin_type,
                "SpriteId": self.sprite_id,
                "SpriteType": self.sprite_type,
                "UserId": self.user_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
