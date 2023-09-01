from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import DrawDesignRaw as _DrawDesignRaw


class DrawDesign(_DrawDesignRaw, _EntityWithIdBase):
    def __init__(self, draw_design_info: _EntityInfo) -> None:
        super().__init__(draw_design_info)
        self._draw_type_enum: _enums.DrawType = _parse.pss_str_enum(self.draw_type, _enums.DrawType)
        self._max_crew_rarity_enum: _enums.CrewRarity = _parse.pss_int_enum(self.max_crew_rarity, _enums.CrewRarity)
        self._min_crew_rarity_enum: _enums.CrewRarity = _parse.pss_int_enum(self.min_crew_rarity, _enums.CrewRarity)

    @property
    def id(self) -> int:
        return self.draw_design_id

    @property
    def draw_type_enum(self) -> "_enums.DrawType":
        return self._draw_type_enum

    @property
    def max_crew_rarity_enum(self) -> "_enums.CrewRarity":
        return self._max_crew_rarity_enum

    @property
    def min_crew_rarity_enum(self) -> "_enums.CrewRarity":
        return self._min_crew_rarity_enum
