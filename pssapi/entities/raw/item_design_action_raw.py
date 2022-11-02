"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ItemDesignActionRaw:
    XML_NODE_NAME: str = 'ItemDesignAction'

    def __init__(self, item_design_action_info: _EntityInfo) -> None:
        self.__condition_type_id: int = _parse.pss_int(
            item_design_action_info.get('ConditionTypeId'))
        self.__action_type_id: int = _parse.pss_int(
            item_design_action_info.get('ActionTypeId'))
        self.__item_design_id: int = _parse.pss_int(
            item_design_action_info.get('ItemDesignId'))
        self.__item_design_action_id: int = _parse.pss_int(
            item_design_action_info.get('ItemDesignActionId'))
        self.__item_design_action_index: int = _parse.pss_int(
            item_design_action_info.get('ItemDesignActionIndex'))

    @property
    def condition_type_id(self) -> int:
        return self.__condition_type_id

    @property
    def action_type_id(self) -> int:
        return self.__action_type_id

    @property
    def item_design_id(self) -> int:
        return self.__item_design_id

    @property
    def item_design_action_id(self) -> int:
        return self.__item_design_action_id

    @property
    def item_design_action_index(self) -> int:
        return self.__item_design_action_index
