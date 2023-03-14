"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomDesignSpriteRaw:
    XML_NODE_NAME: str = "RoomDesignSprite"

    def __init__(self, room_design_sprite_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._animation_id: int = _parse.pss_int(room_design_sprite_info.get("AnimationId"))
        self._flags: int = _parse.pss_int(room_design_sprite_info.get("Flags"))
        self._metadata: str = _parse.pss_str(room_design_sprite_info.get("Metadata"))
        self._race_id: int = _parse.pss_int(room_design_sprite_info.get("RaceId"))
        self._requirement_string: str = _parse.pss_str(room_design_sprite_info.get("RequirementString"))
        self._room_design_id: int = _parse.pss_int(room_design_sprite_info.get("RoomDesignId"))
        self._room_design_sprite_id: int = _parse.pss_int(room_design_sprite_info.get("RoomDesignSpriteId"))
        self._room_effect_parameter: int = _parse.pss_int(room_design_sprite_info.get("RoomEffectParameter"))
        self._room_effect_type: str = _parse.pss_str(room_design_sprite_info.get("RoomEffectType"))
        self._room_sprite_type: str = _parse.pss_str(room_design_sprite_info.get("RoomSpriteType"))
        self._skin_description: str = _parse.pss_str(room_design_sprite_info.get("SkinDescription"))
        self._skin_key: int = _parse.pss_int(room_design_sprite_info.get("SkinKey"))
        self._skin_name: str = _parse.pss_str(room_design_sprite_info.get("SkinName"))
        self._sprite_id: int = _parse.pss_int(room_design_sprite_info.get("SpriteId"))

    @property
    def animation_id(self) -> int:
        return self._animation_id

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def race_id(self) -> int:
        return self._race_id

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def room_design_id(self) -> int:
        return self._room_design_id

    @property
    def room_design_sprite_id(self) -> int:
        return self._room_design_sprite_id

    @property
    def room_effect_parameter(self) -> int:
        return self._room_effect_parameter

    @property
    def room_effect_type(self) -> str:
        return self._room_effect_type

    @property
    def room_sprite_type(self) -> str:
        return self._room_sprite_type

    @property
    def skin_description(self) -> str:
        return self._skin_description

    @property
    def skin_key(self) -> int:
        return self._skin_key

    @property
    def skin_name(self) -> str:
        return self._skin_name

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    def _key(self):
        return (
            self.animation_id,
            self.flags,
            self.metadata,
            self.race_id,
            self.requirement_string,
            self.room_design_id,
            self.room_design_sprite_id,
            self.room_effect_parameter,
            self.room_effect_type,
            self.room_sprite_type,
            self.skin_description,
            self.skin_key,
            self.skin_name,
            self.sprite_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AnimationId": self.animation_id,
                "Flags": self.flags,
                "Metadata": self.metadata,
                "RaceId": self.race_id,
                "RequirementString": self.requirement_string,
                "RoomDesignId": self.room_design_id,
                "RoomDesignSpriteId": self.room_design_sprite_id,
                "RoomEffectParameter": self.room_effect_parameter,
                "RoomEffectType": self.room_effect_type,
                "RoomSpriteType": self.room_sprite_type,
                "SkinDescription": self.skin_description,
                "SkinKey": self.skin_key,
                "SkinName": self.skin_name,
                "SpriteId": self.sprite_id,
            }

        return self._dict
