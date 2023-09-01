from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SituationDesignRaw as _SituationDesignRaw


class SituationDesign(_SituationDesignRaw, _EntityWithIdBase):
    def __init__(self, situation_design_info: _EntityInfo) -> None:
        super().__init__(situation_design_info)
        self._change_type_enum: _enums.ChangeType = _parse.pss_str_enum(self.change_type, _enums.ChangeType)
        self._flags_enum: _enums.SituationDesignFlag = _parse.pss_int_flag(self.flags, _enums.SituationDesignFlag)
        self._situation_type_enum: _enums.SituationType = _parse.pss_str_enum(self.situation_type, _enums.SituationType)
        self._trigger_type_enum: _enums.TriggerType = _parse.pss_str_enum(self.trigger_type, _enums.TriggerType)

    @property
    def id(self) -> int:
        return self.situation_design_id

    @property
    def change_type_enum(self) -> "_enums.ChangeType":
        return self._change_type_enum

    @property
    def flags_enum(self) -> "_enums.SituationDesignFlag":
        return self._flags_enum

    @property
    def situation_type_enum(self) -> "_enums.SituationType":
        return self._situation_type_enum

    @property
    def trigger_type_enum(self) -> "_enums.TriggerType":
        return self._trigger_type_enum
