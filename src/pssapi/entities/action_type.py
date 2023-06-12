from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ActionTypeRaw as _ActionTypeRaw


class ActionType(_ActionTypeRaw, _EntityWithIdBase):
    def __init__(self, action_type_info: _EntityInfo) -> None:
        super().__init__(action_type_info)
        self._action_type_category_enum: _enums.ActionTypeCategory = _parse.pss_str_enum(self.action_type_category, _enums.ActionTypeCategory)
        self._action_type_parameter_relativity_enum: _enums.ActionTypeParameterRelativity = _parse.pss_str_enum(self.action_type_parameter_relativity, _enums.ActionTypeParameterRelativity)
        self._condition_type_category_enum: _enums.ConditionTypeCategory = _parse.pss_str_enum(self.condition_type_category, _enums.ConditionTypeCategory)
        self._condition_type_parameter_enum: _enums.ConditionTypeParameter = _parse.pss_str_enum(self.condition_type_parameter, _enums.ConditionTypeParameter)
        self._room_category_type_enum: _enums.CategoryType = _parse.pss_str_enum(self.room_category_type, _enums.CategoryType)
        self._room_type_enum: _enums.RoomType = _parse.pss_str_enum(self.room_type, _enums.RoomType)

    @property
    def id(self) -> int:
        return self.action_type_id

    @property
    def action_type_category_enum(self) -> "_enums.ActionTypeCategory":
        return self._action_type_category_enum

    @property
    def action_type_parameter_relativity_enum(self) -> "_enums.ActionTypeParameterRelativity":
        return self._action_type_parameter_relativity_enum

    @property
    def condition_type_category_enum(self) -> "_enums.ConditionTypeCategory":
        return self._condition_type_category_enum

    @property
    def condition_type_parameter_enum(self) -> "_enums.ConditionTypeParameter":
        return self._condition_type_parameter_enum

    @property
    def room_category_type_enum(self) -> "_enums.CategoryType":
        return self._room_category_type_enum

    @property
    def room_type_enum(self) -> "_enums.RoomType":
        return self._room_type_enum
