from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CollectionDesignRaw as _CollectionDesignRaw


class CollectionDesign(_CollectionDesignRaw, _EntityWithIdBase):
    def __init__(self, collection_design_info: _EntityInfo) -> None:
        super().__init__(collection_design_info)

    @property
    def id(self) -> int:
        return self.collection_design_id
