####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomActionRaw():
    XML_NODE_NAME: str = 'RoomAction'

    def __init__(self, room_action_info: _EntityInfo) -> None:
        self.__room_action_id: int = _parse.pss_int(room_action_info.get('RoomActionId'))
        self.__room_id: int = _parse.pss_int(room_action_info.get('RoomId'))
        self.__room_action_index: int = _parse.pss_int(room_action_info.get('RoomActionIndex'))
        self.__condition_type_id: int = _parse.pss_int(room_action_info.get('ConditionTypeId'))
        self.__action_type_id: int = _parse.pss_int(room_action_info.get('ActionTypeId'))

    @property
    def room_action_id(self) -> int:
        return self.__room_action_id

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def room_action_index(self) -> int:
        return self.__room_action_index

    @property
    def condition_type_id(self) -> int:
        return self.__condition_type_id

    @property
    def action_type_id(self) -> int:
        return self.__action_type_id
