
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import PromotionDesignRaw as _PromotionDesignRaw
from ..types import EntityInfo as _EntityInfo


class PromotionDesign(_EntityWithIdBase, _PromotionDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<PromotionDesign {self.id}>'

    def __str__(self) -> str:
        return f'<PromotionDesign {self.id}>'

    @property
    def id(self) -> int:
        return self.promotion_design_id
