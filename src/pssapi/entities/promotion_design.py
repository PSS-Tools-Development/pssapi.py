from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import PromotionDesignRaw as _PromotionDesignRaw


class PromotionDesign(_PromotionDesignRaw, _EntityWithIdBase):
    def __init__(self, promotion_design_info: _EntityInfo) -> None:
        super().__init__(promotion_design_info)

    @property
    def id(self) -> int:
        return self.promotion_design_id
