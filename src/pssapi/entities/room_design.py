from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import RoomDesignMetadata as _RoomDesignMetadata
from .raw import RoomDesignRaw as _RoomDesignRaw


class RoomDesign(_RoomDesignRaw, _EntityWithIdBase):
    def __init__(self, room_design_info: _EntityInfo) -> None:
        super().__init__(room_design_info)
        self._category_type_enum: _enums.CategoryType = _parse.pss_str_enum(self.category_type, _enums.CategoryType)
        self._enhancement_type_enum: _enums.EnhancementType = _parse.pss_str_enum(self.enhancement_type, _enums.EnhancementType)
        self._flags_enum: _enums.RoomFlags = _parse.pss_int_flag(self.flags, _enums.RoomFlags)
        self._manufacture_type_enum: _enums.ManufactureType = _parse.pss_str_enum(self.manufacture_type, _enums.ManufactureType)
        self._room_design_metadata: _RoomDesignMetadata = _RoomDesignMetadata(self.metadata)
        self._room_type_enum: _enums.RoomType = _parse.pss_str_enum(self.room_type, _enums.RoomType)
        self._supported_grid_types_enum: _enums.GridTypeFlag = _parse.pss_int_flag(self.supported_grid_types, _enums.GridTypeFlag)
        self._target_type_enum: _enums.TargetType = _parse.pss_str_enum(self.target_type, _enums.TargetType)

    @property
    def id(self) -> int:
        return self.room_design_id

    @property
    def category_type_enum(self) -> "_enums.CategoryType":
        return self._category_type_enum

    @property
    def enhancement_type_enum(self) -> "_enums.EnhancementType":
        return self._enhancement_type_enum

    @property
    def flags_enum(self) -> "_enums.RoomFlags":
        return self._flags_enum

    @property
    def manufacture_type_enum(self) -> "_enums.ManufactureType":
        return self._manufacture_type_enum

    @property
    def room_design_metadata(self) -> _RoomDesignMetadata:
        return self._room_design_metadata

    @property
    def room_type_enum(self) -> "_enums.RoomType":
        return self._room_type_enum

    @property
    def supported_grid_types_enum(self) -> "_enums.GridTypeFlag":
        return self._supported_grid_types_enum

    @property
    def target_type_enum(self) -> "_enums.TargetType":
        return self._target_type_enum
