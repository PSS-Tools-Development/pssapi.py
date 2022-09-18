
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import TrainingDesignRaw as _TrainingDesignRaw
from ..types import EntityInfo as _EntityInfo


class TrainingDesign(_EntityWithIdBase, _TrainingDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<TrainingDesign {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<TrainingDesign {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.training_design_id
