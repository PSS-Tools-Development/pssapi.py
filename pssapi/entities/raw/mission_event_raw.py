####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MissionEventRaw():
    XML_NODE_NAME: str = 'MissionEvent'

    def __init__(self, mission_event_info: _EntityInfo) -> None:
        self.__mission_event_id: int = _parse.pss_int(mission_event_info.get('MissionEventId'))
        self.__mission_design_id: int = _parse.pss_int(mission_event_info.get('MissionDesignId'))
        self.__percent_weight: int = _parse.pss_int(mission_event_info.get('PercentWeight'))
        self.__start_description: str = _parse.pss_str(mission_event_info.get('StartDescription'))
        self.__end_description: str = _parse.pss_str(mission_event_info.get('EndDescription'))
        self.__time_limit: int = _parse.pss_int(mission_event_info.get('TimeLimit'))
        self.__mission_event_type: str = _parse.pss_str(mission_event_info.get('MissionEventType'))
        self.__event_xml_string: str = _parse.pss_str(mission_event_info.get('EventXmlString'))
        self.__title: str = _parse.pss_str(mission_event_info.get('Title'))
        self.__is_single_play: bool = _parse.pss_bool(mission_event_info.get('IsSinglePlay'))
        self.__reward_string: str = _parse.pss_str(mission_event_info.get('RewardString'))
        self.__requirement_string: str = _parse.pss_str(mission_event_info.get('RequirementString'))
        self.__cost_string: str = _parse.pss_str(mission_event_info.get('CostString'))
        self.__function_string: str = _parse.pss_str(mission_event_info.get('FunctionString'))
        self.__requirement_description: str = _parse.pss_str(mission_event_info.get('RequirementDescription'))
        self.__parent_mission_event_id: int = _parse.pss_int(mission_event_info.get('ParentMissionEventId'))
        self.__background_id: int = _parse.pss_int(mission_event_info.get('BackgroundId'))
        self.__ship_id: int = _parse.pss_int(mission_event_info.get('ShipId'))
        self.__background_sprite_id: int = _parse.pss_int(mission_event_info.get('BackgroundSpriteId'))

    @property
    def mission_event_id(self) -> int:
        return self.__mission_event_id

    @property
    def mission_design_id(self) -> int:
        return self.__mission_design_id

    @property
    def percent_weight(self) -> int:
        return self.__percent_weight

    @property
    def start_description(self) -> str:
        return self.__start_description

    @property
    def end_description(self) -> str:
        return self.__end_description

    @property
    def time_limit(self) -> int:
        return self.__time_limit

    @property
    def mission_event_type(self) -> str:
        return self.__mission_event_type

    @property
    def event_xml_string(self) -> str:
        return self.__event_xml_string

    @property
    def title(self) -> str:
        return self.__title

    @property
    def is_single_play(self) -> bool:
        return self.__is_single_play

    @property
    def reward_string(self) -> str:
        return self.__reward_string

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def cost_string(self) -> str:
        return self.__cost_string

    @property
    def function_string(self) -> str:
        return self.__function_string

    @property
    def requirement_description(self) -> str:
        return self.__requirement_description

    @property
    def parent_mission_event_id(self) -> int:
        return self.__parent_mission_event_id

    @property
    def background_id(self) -> int:
        return self.__background_id

    @property
    def ship_id(self) -> int:
        return self.__ship_id

    @property
    def background_sprite_id(self) -> int:
        return self.__background_sprite_id
