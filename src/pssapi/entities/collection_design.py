from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CollectionDesignRaw as _CollectionDesignRaw


class CollectionDesign(_CollectionDesignRaw, _EntityWithIdBase):
    def __init__(self, collection_design_info: _EntityInfo) -> None:
        super().__init__(collection_design_info)
        self._collection_type_enum: _enums.CollectionType = _parse.pss_str_enum(self.collection_type, _enums.CollectionType)
        self._enhancement_type_enum: _enums.EnhancementType = _parse.pss_str_enum(self.enhancement_type, _enums.EnhancementType)
        # self._flags_enum: _enums. = _parse.pss_str_enum(self.flags, _enums.)   # This enum does not exist up to PSS v0.994.1

    @property
    def id(self) -> int:
        return self.collection_design_id

    @property
    def collection_type_enum(self) -> "_enums.CollectionType":
        return self._collection_type_enum

    @property
    def enhancement_type_enum(self) -> "_enums.EnhancementType":
        return self._enhancement_type_enum
