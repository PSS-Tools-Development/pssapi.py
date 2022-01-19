"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MissionEventRaw:
    XML_NODE_NAME: str = "MissionEvent"

    def __init__(self, mission_event_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._background_id: int = _parse.pss_int(mission_event_info.get("BackgroundId"))
        self._background_sprite_id: int = _parse.pss_int(mission_event_info.get("BackgroundSpriteId"))
        self._cost_string: str = _parse.pss_str(mission_event_info.get("CostString"))
        self._end_description: str = _parse.pss_str(mission_event_info.get("EndDescription"))
        self._event_xml_string: str = _parse.pss_str(mission_event_info.get("EventXmlString"))
        self._flags: int = _parse.pss_int(mission_event_info.get("Flags"))
        self._function_string: str = _parse.pss_str(mission_event_info.get("FunctionString"))
        self._is_single_play: bool = _parse.pss_bool(mission_event_info.get("IsSinglePlay"))
        self._mission_design_id: int = _parse.pss_int(mission_event_info.get("MissionDesignId"))
        self._mission_event_id: int = _parse.pss_int(mission_event_info.get("MissionEventId"))
        self._mission_event_type: str = _parse.pss_str(mission_event_info.get("MissionEventType"))
        self._parent_mission_event_id: int = _parse.pss_int(mission_event_info.get("ParentMissionEventId"))
        self._percent_weight: int = _parse.pss_int(mission_event_info.get("PercentWeight"))
        self._requirement_description: str = _parse.pss_str(mission_event_info.get("RequirementDescription"))
        self._requirement_string: str = _parse.pss_str(mission_event_info.get("RequirementString"))
        self._reward_string: str = _parse.pss_str(mission_event_info.get("RewardString"))
        self._ship_id: int = _parse.pss_int(mission_event_info.get("ShipId"))
        self._start_description: str = _parse.pss_str(mission_event_info.get("StartDescription"))
        self._time_limit: int = _parse.pss_int(mission_event_info.get("TimeLimit"))
        self._title: str = _parse.pss_str(mission_event_info.get("Title"))

    @property
    def background_id(self) -> int:
        return self._background_id

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def cost_string(self) -> str:
        return self._cost_string

    @property
    def end_description(self) -> str:
        return self._end_description

    @property
    def event_xml_string(self) -> str:
        return self._event_xml_string

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def function_string(self) -> str:
        return self._function_string

    @property
    def is_single_play(self) -> bool:
        return self._is_single_play

    @property
    def mission_design_id(self) -> int:
        return self._mission_design_id

    @property
    def mission_event_id(self) -> int:
        return self._mission_event_id

    @property
    def mission_event_type(self) -> str:
        return self._mission_event_type

    @property
    def parent_mission_event_id(self) -> int:
        return self._parent_mission_event_id

    @property
    def percent_weight(self) -> int:
        return self._percent_weight

    @property
    def requirement_description(self) -> str:
        return self._requirement_description

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def reward_string(self) -> str:
        return self._reward_string

    @property
    def ship_id(self) -> int:
        return self._ship_id

    @property
    def start_description(self) -> str:
        return self._start_description

    @property
    def time_limit(self) -> int:
        return self._time_limit

    @property
    def title(self) -> str:
        return self._title

    def _key(self):
        return (
            self.background_id,
            self.background_sprite_id,
            self.cost_string,
            self.end_description,
            self.event_xml_string,
            self.flags,
            self.function_string,
            self.is_single_play,
            self.mission_design_id,
            self.mission_event_id,
            self.mission_event_type,
            self.parent_mission_event_id,
            self.percent_weight,
            self.requirement_description,
            self.requirement_string,
            self.reward_string,
            self.ship_id,
            self.start_description,
            self.time_limit,
            self.title,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BackgroundId": self.background_id,
                "BackgroundSpriteId": self.background_sprite_id,
                "CostString": self.cost_string,
                "EndDescription": self.end_description,
                "EventXmlString": self.event_xml_string,
                "Flags": self.flags,
                "FunctionString": self.function_string,
                "IsSinglePlay": self.is_single_play,
                "MissionDesignId": self.mission_design_id,
                "MissionEventId": self.mission_event_id,
                "MissionEventType": self.mission_event_type,
                "ParentMissionEventId": self.parent_mission_event_id,
                "PercentWeight": self.percent_weight,
                "RequirementDescription": self.requirement_description,
                "RequirementString": self.requirement_string,
                "RewardString": self.reward_string,
                "ShipId": self.ship_id,
                "StartDescription": self.start_description,
                "TimeLimit": self.time_limit,
                "Title": self.title,
            }

        return self._dict
