from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ItemRaw as _ItemRaw


class Item(_ItemRaw, _EntityWithIdBase):
    def __init__(self, item_info: _EntityInfo) -> None:
        super().__init__(item_info)
        self._bonus_enhancement_type_enum: _enums.EnhancementType = _parse.pss_str_enum(self.bonus_enhancement_type, _enums.EnhancementType)

    @property
    def id(self) -> int:
        return self.item_id

    @property
    def bonus_enhancement_type_enum(self) -> "_enums.EnhancementType":
        return self._bonus_enhancement_type_enum
