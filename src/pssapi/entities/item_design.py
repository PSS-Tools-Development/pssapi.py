from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import ItemDesignMetadata as _ItemDesignMetadata
from .raw import ItemDesignRaw as _ItemDesignRaw


class ItemDesign(_ItemDesignRaw, _EntityWithIdBase):
    def __init__(self, item_design_info: _EntityInfo) -> None:
        super().__init__(item_design_info)
        self._enhancement_type_enum: _enums.EnhancementType = _parse.pss_str_enum(self.enhancement_type, _enums.EnhancementType)
        self._flags_enum: _enums.ItemDesignFlagType = _parse.pss_int_flag(self.flags, _enums.ItemDesignFlagType)
        self._item_design_metadata: _ItemDesignMetadata = _ItemDesignMetadata(self.metadata)
        self._item_sub_type_enum: _enums.ItemSubType = _parse.pss_str_enum(self.item_sub_type, _enums.ItemSubType)
        self._item_type_enum: _enums.ItemType = _parse.pss_str_enum(self.item_type, _enums.ItemType)
        self._module_type_enum: _enums.ModuleType = _parse.pss_str_enum(self.module_type, _enums.ModuleType)
        self._rarity_enum: _enums.Rarity = _parse.pss_str_enum(self.rarity, _enums.Rarity)

    @property
    def id(self) -> int:
        return self.item_design_id

    @property
    def enhancement_type_enum(self) -> "_enums.EnhancementType":
        return self._enhancement_type_enum

    @property
    def flags_enum(self) -> "_enums.ItemDesignFlagType":
        return self._flags_enum

    @property
    def item_design_metadata(self) -> _ItemDesignMetadata:
        return self._item_design_metadata

    @property
    def item_sub_type_enum(self) -> "_enums.ItemSubType":
        return self._item_sub_type_enum

    @property
    def item_type_enum(self) -> "_enums.ItemType":
        return self._item_type_enum

    @property
    def module_type_enum(self) -> "_enums.ItemType":
        return self._module_type_enum

    @property
    def rarity_enum(self) -> "_enums.Rarity":
        return self._rarity_enum
