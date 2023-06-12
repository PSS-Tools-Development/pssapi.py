from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import ItemDesignMetadata as _ItemDesignMetadata
from .raw import ItemDesignRaw as _ItemDesignRaw


class ItemDesign(_ItemDesignRaw, _EntityWithIdBase):
    def __init__(self, item_design_info: _EntityInfo) -> None:
        super().__init__(item_design_info)
        self._item_design_metadata: _ItemDesignMetadata = _ItemDesignMetadata(self.metadata)

    @property
    def id(self) -> int:
        return self.item_design_id

    @property
    def item_design_metadata(self) -> _ItemDesignMetadata:
        return self._item_design_metadata
