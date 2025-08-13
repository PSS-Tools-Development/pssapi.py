from .entity_base import EntityWithIdBase
from .raw import DivisionDesignRaw


class DivisionDesign(DivisionDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.division_design_id


__all__ = [
    "DivisionDesign",
]
