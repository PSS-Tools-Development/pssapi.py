from .entity_base import EntityWithIdBase
from .raw import TrainingDesignRaw


class TrainingDesign(TrainingDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.training_design_id


__all__ = [
    "TrainingDesign",
]
