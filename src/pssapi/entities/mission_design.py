from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import MissionDesignRaw as _MissionDesignRaw


class MissionDesign(_MissionDesignRaw, _EntityWithIdBase):
    def __init__(self, mission_design_info: _EntityInfo) -> None:
        super().__init__(mission_design_info)

    @property
    def id(self) -> int:
        return self.mission_design_id
