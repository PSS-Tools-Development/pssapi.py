
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import MissionDesignRaw as _MissionDesignRaw
from ..types import EntityInfo as _EntityInfo


class MissionDesign(_EntityWithIdBase, _MissionDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<MissionDesign {self.id}>'

    def __str__(self) -> str:
        return f'<MissionDesign {self.id}>'

    @property
    def id(self) -> int:
        return self.mission_design_id
