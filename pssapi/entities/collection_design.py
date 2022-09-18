
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CollectionDesignRaw as _CollectionDesignRaw
from ..types import EntityInfo as _EntityInfo


class CollectionDesign(_EntityWithIdBase, _CollectionDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<CollectionDesign {self.id}: {self.name}>'

    def __str__(self) -> str:
        return f'<CollectionDesign {self.id}: {self.name}>'

    @property
    def id(self) -> int:
        return self.collection_design_id
