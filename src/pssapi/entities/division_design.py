from typing import List as _List

from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import DivisionDesignRaw as _DivisionDesignRaw


class DivisionDesign(_DivisionDesignRaw, _EntityWithIdBase):
    def __init__(self, division_design_info: _EntityInfo) -> None:
        super().__init__(division_design_info)
        self._division_type_enum: _enums.DivisionType = _parse.pss_str_enum(self.division_type, _enums.DivisionType)
        self._banner_sprite_ids_list: _List[int] = [int(x) for x in _parse.pss_str_list(self.banner_sprite_ids)]
        self._monthly_achievement_design_ids_list: _List[int] = [int(x) for x in _parse.pss_str_list(self.monthly_achievement_design_ids)]
        self._yearly_achievement_design_ids_list: _List[int] = [int(x) for x in _parse.pss_str_list(self.yearly_achievement_design_ids)]

    @property
    def id(self) -> int:
        return self.division_design_id

    @property
    def division_type_enum(self) -> "_enums.DivisionType":
        return self._division_type_enum

    @property
    def banner_sprite_ids_list(self) -> _List[int]:
        return self._banner_sprite_ids_list

    @property
    def monthly_achievement_design_ids_list(self) -> _List[int]:
        return self._monthly_achievement_design_ids_list

    @property
    def yearly_achievement_design_ids_list(self) -> _List[int]:
        return self._yearly_achievement_design_ids_list
