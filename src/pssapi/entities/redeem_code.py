from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import RedeemCodeRaw as _RedeemCodeRaw


class RedeemCode(_RedeemCodeRaw, _EntityBase):
    def __init__(self, redeem_code_info: _EntityInfo) -> None:
        super().__init__(redeem_code_info)
