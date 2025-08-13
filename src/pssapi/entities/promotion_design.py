from .entity_base import EntityWithIdBase
from .raw import PromotionDesignRaw


class PromotionDesign(PromotionDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.promotion_design_id


__all__ = [
    "PromotionDesign",
]
