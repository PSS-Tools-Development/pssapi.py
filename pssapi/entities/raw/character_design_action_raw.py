"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterDesignActionRaw:
    XML_NODE_NAME: str = 'CharacterDesignAction'

    def __init__(self, character_design_action_info: _EntityInfo) -> None:
        self.__character_design_action_id: int = _parse.pss_int(
            character_design_action_info.get('CharacterDesignActionId'))
        self.__character_design_id: int = _parse.pss_int(
            character_design_action_info.get('CharacterDesignId'))
        self.__character_design_action_index: int = _parse.pss_int(
            character_design_action_info.get('CharacterDesignActionIndex'))
        self.__condition_type_id: int = _parse.pss_int(
            character_design_action_info.get('ConditionTypeId'))
        self.__action_type_id: int = _parse.pss_int(
            character_design_action_info.get('ActionTypeId'))

    @property
    def character_design_action_id(self) -> int:
        return self.__character_design_action_id

    @property
    def character_design_id(self) -> int:
        return self.__character_design_id

    @property
    def character_design_action_index(self) -> int:
        return self.__character_design_action_index

    @property
    def condition_type_id(self) -> int:
        return self.__condition_type_id

    @property
    def action_type_id(self) -> int:
        return self.__action_type_id
