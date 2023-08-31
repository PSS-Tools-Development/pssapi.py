from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import SkinMetadata as _SkinMetadata
from .raw import SkinRaw as _SkinRaw


class Skin(_SkinRaw, _EntityWithIdBase):
    def __init__(self, skin_info: _EntityInfo) -> None:
        super().__init__(skin_info)
        self._skin_type_enum: _enums.RoomStatus = _parse.pss_str_enum(self.skin_type, _enums.SkinType)
        self._skin_metadata: _SkinMetadata = _SkinMetadata(self.metadata)
        self._sprite_type_enum: _enums.RoomSpriteType = _parse.pss_str_enum(self.sprite_type, _enums.RoomSpriteType)

    @property
    def id(self) -> int:
        return self.skin_id

    @property
    def skin_metadata(self) -> _SkinMetadata:
        return self._skin_metadata

    @property
    def skin_type_enum(self) -> "_enums.SkinType":
        return self._skin_type_enum

    @property
    def sprite_type_enum(self) -> "_enums.RoomSpriteType":
        return self._sprite_type_enum
