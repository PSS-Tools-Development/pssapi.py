from .entity_base import EntityWithIdBase
from .raw import CollectionDesignRaw


class CollectionDesign(CollectionDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.collection_design_id


__all__ = [
    "CollectionDesign",
]
