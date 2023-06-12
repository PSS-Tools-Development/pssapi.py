from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import RoomDesignSpriteMetadata as _RoomDesignSpriteMetadata
from .raw import RoomDesignSpriteRaw as _RoomDesignSpriteRaw


class RoomDesignSprite(_RoomDesignSpriteRaw, _EntityWithIdBase):
    def __init__(self, room_design_sprite_info: _EntityInfo) -> None:
        super().__init__(room_design_sprite_info)
        self._flags_enum: _enums.RoomDesignSpriteFlag = _parse.pss_int_flag(self.flags, _enums.RoomDesignSpriteFlag)
        self._room_design_sprite_metadata: _RoomDesignSpriteMetadata = _RoomDesignSpriteMetadata(self.metadata)
        self._room_effect_type_enum: _enums.RoomEffectType = _parse.pss_str_enum(self.room_effect_type, _enums.RoomEffectType)
        self._room_sprite_type_enum: _enums.RoomSpriteType = _parse.pss_str_enum(self.room_sprite_type, _enums.RoomSpriteType)

    @property
    def id(self) -> int:
        return self.room_design_sprite_id

    @property
    def flags_enum(self) -> "_enums.RoomDesignSpriteFlag":
        return self._flags_enum

    @property
    def room_design_sprite_metadata(self) -> _RoomDesignSpriteMetadata:
        return self._room_design_sprite_metadata

    @property
    def room_effect_type_enum(self) -> "_enums.RoomEffectType":
        return self._room_effect_type_enum

    @property
    def room_sprite_type_enum(self) -> "_enums.RoomSpriteType":
        return self._room_sprite_type_enum
