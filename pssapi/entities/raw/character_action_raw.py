####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterActionRaw():
    XML_NODE_NAME: str = 'CharacterAction'

    def __init__(self, character_action_info: _EntityInfo) -> None:
        self.__character_action_id: int = _parse.pss_int(character_action_info.get('CharacterActionId'))
        self.__condition_type_id: int = _parse.pss_int(character_action_info.get('ConditionTypeId'))
        self.__character_action_index: int = _parse.pss_int(character_action_info.get('CharacterActionIndex'))
        self.__action_type_id: int = _parse.pss_int(character_action_info.get('ActionTypeId'))
        self.__character_id: int = _parse.pss_int(character_action_info.get('CharacterId'))

    @property
    def character_action_id(self) -> int:
        return self.__character_action_id

    @property
    def condition_type_id(self) -> int:
        return self.__condition_type_id

    @property
    def character_action_index(self) -> int:
        return self.__character_action_index

    @property
    def action_type_id(self) -> int:
        return self.__action_type_id

    @property
    def character_id(self) -> int:
        return self.__character_id
