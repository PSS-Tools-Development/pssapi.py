from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import TrainingDesignRaw as _TrainingDesignRaw


class TrainingDesign(_TrainingDesignRaw, _EntityWithIdBase):
    def __init__(self, training_design_info: _EntityInfo) -> None:
        super().__init__(training_design_info)

    @property
    def id(self) -> int:
        return self.training_design_id
