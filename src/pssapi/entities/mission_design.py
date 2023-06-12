from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import MissionDesignMetadata as _MissionDesignMetadata
from .raw import MissionDesignRaw as _MissionDesignRaw


class MissionDesign(_MissionDesignRaw, _EntityWithIdBase):
    def __init__(self, mission_design_info: _EntityInfo) -> None:
        super().__init__(mission_design_info)
        self._flags_enum: _enums.MissionDesignFlag = _parse.pss_int_flag(self.flags, _enums.MissionDesignFlag)
        self._mission_design_metadata: _MissionDesignMetadata = _MissionDesignMetadata(self.metadata)
        self._mission_design_status_enum: _enums.MissionDesignStatus = _parse.pss_str_enum(self.mission_design_status, _enums.MissionDesignStatus)
        self._mission_design_type_enum: _enums.MissionDesignType = _parse.pss_str_enum(self.mission_design_type, _enums.MissionDesignType)

    @property
    def id(self) -> int:
        return self.mission_design_id

    @property
    def flags_enum(self) -> "_enums.MissionDesignFlag":
        return self._flags_enum

    @property
    def mission_design_metadata(self) -> _MissionDesignMetadata:
        return self._mission_design_metadata

    @property
    def mission_design_status_enum(self) -> "_enums.MissionDesignStatus":
        return self._mission_design_status_enum

    @property
    def mission_design_type_enum(self) -> "_enums.MissionDesignType":
        return self._mission_design_type_enum
