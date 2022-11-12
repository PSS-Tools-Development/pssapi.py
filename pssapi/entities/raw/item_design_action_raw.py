"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ItemDesignActionRaw:
    XML_NODE_NAME: str = 'ItemDesignAction'

    def __init__(self, item_design_action_info: _EntityInfo) -> None:
        self.action_type_id: int = _parse.pss_int(
            item_design_action_info.get('ActionTypeId'))
        self.condition_type_id: int = _parse.pss_int(
            item_design_action_info.get('ConditionTypeId'))
        self.item_design_action_id: int = _parse.pss_int(
            item_design_action_info.get('ItemDesignActionId'))
        self.item_design_action_index: int = _parse.pss_int(
            item_design_action_info.get('ItemDesignActionIndex'))
        self.item_design_id: int = _parse.pss_int(
            item_design_action_info.get('ItemDesignId'))
