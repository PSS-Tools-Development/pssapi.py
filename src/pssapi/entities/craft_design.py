from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CraftDesignRaw as _CraftDesignRaw


class CraftDesign(_CraftDesignRaw, _EntityWithIdBase):
    def __init__(self, craft_design_info: _EntityInfo) -> None:
        super().__init__(craft_design_info)
        self._craft_attack_type_enum: _enums.CraftAttackType = _parse.pss_str_enum(self.craft_attack_type, _enums.CraftAttackType)
        self._craft_target_type_enum: _enums.CraftTargetType = _parse.pss_str_enum(self.craft_target_type, _enums.CraftTargetType)

    @property
    def id(self) -> int:
        return self.craft_design_id

    @property
    def craft_attack_type_enum(self) -> "_enums.CraftAttackType":
        return self._craft_attack_type_enum

    @property
    def craft_target_type_enum(self) -> "_enums.CraftTargetType":
        return self._craft_target_type_enum
