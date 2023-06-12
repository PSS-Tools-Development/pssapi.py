from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import PromotionDesignMetadata as _PromotionDesignMetadata
from .raw import PromotionDesignRaw as _PromotionDesignRaw


class PromotionDesign(_PromotionDesignRaw, _EntityWithIdBase):
    def __init__(self, promotion_design_info: _EntityInfo) -> None:
        super().__init__(promotion_design_info)
        self._promotion_design_metadata: _PromotionDesignMetadata = _PromotionDesignMetadata(self.metadata)

    @property
    def id(self) -> int:
        return self.promotion_design_id

    @property
    def promotion_design_metadata(self) -> _PromotionDesignMetadata:
        return self._promotion_design_metadata
