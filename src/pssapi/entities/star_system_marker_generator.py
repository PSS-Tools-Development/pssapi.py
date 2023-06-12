from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import StarSystemMarkerGeneratorMetadata as _StarSystemMarkerGeneratorMetadata
from .raw import StarSystemMarkerGeneratorRaw as _StarSystemMarkerGeneratorRaw


class StarSystemMarkerGenerator(_StarSystemMarkerGeneratorRaw, _EntityWithIdBase):
    def __init__(self, star_system_marker_generator_info: _EntityInfo) -> None:
        super().__init__(star_system_marker_generator_info)
        self._behavior_flags_enum: _enums.BehaviorFlags = _parse.pss_int_flag(self.behavior_flags, _enums.BehaviorFlags)
        self._completion_value_type_enum: _enums.CompletionValueType = _parse.pss_str_enum(self.completion_value_type, _enums.CompletionValueType)
        self._cost_type_enum: _enums.CostType = _parse.pss_str_enum(self.cost_type, _enums.CostType)
        self._generation_flags_enum: _enums.GenerationFlags = _parse.pss_int_flag(self.generation_flags, _enums.GenerationFlags)
        self._marker_flags_enum: _enums.MarkerFlag = _parse.pss_int_flag(self.marker_flags, _enums.MarkerFlag)
        self._marker_type_enum: _enums.MarkerType = _parse.pss_str_enum(self.marker_type, _enums.MarkerType)
        self._movement_type_enum: _enums.MovementType = _parse.pss_str_enum(self.movement_type, _enums.MovementType)
        self._star_system_marker_generator_metadata: _StarSystemMarkerGeneratorMetadata = _StarSystemMarkerGeneratorMetadata(self.metadata)

    @property
    def id(self) -> int:
        return self.star_system_marker_generator_id

    @property
    def behavior_flags_enum(self) -> "_enums.BehaviorFlags":
        return self._behavior_flags_enum

    @property
    def completion_value_type_enum(self) -> "_enums.CompletionValueType":
        return self._completion_value_type_enum

    @property
    def cost_type_enum(self) -> "_enums.CostType":
        return self._cost_type_enum

    @property
    def generation_flags_enum(self) -> "_enums.GenerationFlags":
        return self._generation_flags_enum

    @property
    def marker_flags_enum(self) -> "_enums.MarkerFlag":
        return self._marker_flags_enum

    @property
    def marker_type_enum(self) -> "_enums.MarkerType":
        return self._marker_type_enum

    @property
    def movement_type_enum(self) -> "_enums.MovementType":
        return self._movement_type_enum

    @property
    def star_system_marker_generator_metadata(self) -> _StarSystemMarkerGeneratorMetadata:
        return self._star_system_marker_generator_metadata
