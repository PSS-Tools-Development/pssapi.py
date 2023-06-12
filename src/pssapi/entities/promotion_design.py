from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import PromotionDesignMetadata as _PromotionDesignMetadata
from .raw import PromotionDesignRaw as _PromotionDesignRaw


class PromotionDesign(_PromotionDesignRaw, _EntityWithIdBase):
    def __init__(self, promotion_design_info: _EntityInfo) -> None:
        super().__init__(promotion_design_info)
        self._flags_enum: _enums.PromotionDesignFlag = _parse.pss_int_flag(self.flags, _enums.PromotionDesignFlag)
        self._promotion_design_metadata: _PromotionDesignMetadata = _PromotionDesignMetadata(self.metadata)
        self._promotion_type_enum: _enums.PromotionType = _parse.pss_str_enum(self.promotion_type, _enums.PromotionType)
        self._purchase_mask_enum: _enums.SaleItemMask = _parse.pss_int_flag(self.purchase_mask, _enums.SaleItemMask)

    @property
    def id(self) -> "_enums.PromotionDesignFlag":
        return self.promotion_design_id

    @property
    def flags_enum(self) -> int:
        return self._flags_enum

    @property
    def promotion_design_metadata(self) -> _PromotionDesignMetadata:
        return self._promotion_design_metadata

    @property
    def promotion_type_enum(self) -> "_enums.PromotionType":
        return self._promotion_type_enum

    @property
    def purchase_mask_enum(self) -> "_enums.SaleItemMask":
        return self._purchase_mask_enum
