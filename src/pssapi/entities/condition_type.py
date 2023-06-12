from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ConditionTypeRaw as _ConditionTypeRaw


class ConditionType(_ConditionTypeRaw, _EntityWithIdBase):
    def __init__(self, condition_type_info: _EntityInfo) -> None:
        super().__init__(condition_type_info)
        self._condition_type_availability_enum: _enums.ConditionTypeAvailabilityMask = _parse.pss_int_flag(self.condition_type_availability, _enums.ConditionTypeAvailabilityMask)
        self._condition_type_category_enum: _enums.ConditionTypeCategory = _parse.pss_str_enum(self.condition_type_category, _enums.ConditionTypeCategory)
        self._condition_type_comparison_enum: _enums.ConditionTypeComparison = _parse.pss_str_enum(self.condition_type_comparison, _enums.ConditionTypeComparison)
        self._condition_type_parameter_enum: _enums.ConditionTypeParameter = _parse.pss_str_enum(self.condition_type_parameter, _enums.ConditionTypeParameter)
        self._room_category_type_enum: _enums.CategoryType = _parse.pss_str_enum(self.room_category_type, _enums.CategoryType)
        self._room_type_enum: _enums.RoomType = _parse.pss_str_enum(self.room_type, _enums.RoomType)

    @property
    def id(self) -> int:
        return self.condition_type_id

    @property
    def condition_type_availability_enum(self) -> "_enums.ConditionTypeAvailabilityMask":
        return self._condition_type_availability_enum

    @property
    def condition_type_category_enum(self) -> "_enums.ConditionTypeCategory":
        return self._condition_type_category_enum

    @property
    def condition_type_comparison_enum(self) -> "_enums.ConditionTypeComparison":
        return self._condition_type_comparison_enum

    @property
    def condition_type_parameter_enum(self) -> "_enums.ConditionTypeParameter":
        return self._condition_type_parameter_enum

    @property
    def room_category_type_enum(self) -> "_enums.CategoryType":
        return self._room_category_type_enum

    @property
    def room_type_enum(self) -> "_enums.RoomType":
        return self._room_type_enum
