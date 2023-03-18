"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MissionDesignRaw:
    XML_NODE_NAME: str = "MissionDesign"

    def __init__(self, mission_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._available_every_x_days: int = _parse.pss_int(mission_design_info.get("AvailableEveryXDays"))
        self._available_from: _datetime = _parse.pss_datetime(mission_design_info.get("AvailableFrom"))
        self._available_to: _datetime = _parse.pss_datetime(mission_design_info.get("AvailableTo"))
        self._background_sprite_id: int = _parse.pss_int(mission_design_info.get("BackgroundSpriteId"))
        self._chance: int = _parse.pss_int(mission_design_info.get("Chance"))
        self._condition: str = _parse.pss_str(mission_design_info.get("Condition"))
        self._exploration_percentage: int = _parse.pss_int(mission_design_info.get("ExplorationPercentage"))
        self._flags: int = _parse.pss_int(mission_design_info.get("Flags"))
        self._is_single_play: bool = _parse.pss_bool(mission_design_info.get("IsSinglePlay"))
        self._max_attempts_per_day: int = _parse.pss_int(mission_design_info.get("MaxAttemptsPerDay"))
        self._max_ship_level: int = _parse.pss_int(mission_design_info.get("MaxShipLevel"))
        self._metadata: str = _parse.pss_str(mission_design_info.get("Metadata"))
        self._min_duration_since_last_event: int = _parse.pss_int(mission_design_info.get("MinDurationSinceLastEvent"))
        self._min_ship_level: int = _parse.pss_int(mission_design_info.get("MinShipLevel"))
        self._mission_description: str = _parse.pss_str(mission_design_info.get("MissionDescription"))
        self._mission_design_id: int = _parse.pss_int(mission_design_info.get("MissionDesignId"))
        self._mission_design_status: str = _parse.pss_str(mission_design_info.get("MissionDesignStatus"))
        self._mission_design_type: str = _parse.pss_str(mission_design_info.get("MissionDesignType"))
        self._mission_title: str = _parse.pss_str(mission_design_info.get("MissionTitle"))
        self._required_mission_design_id: int = _parse.pss_int(mission_design_info.get("RequiredMissionDesignId"))
        self._requirement_description: str = _parse.pss_str(mission_design_info.get("RequirementDescription"))
        self._requirement_string: str = _parse.pss_str(mission_design_info.get("RequirementString"))
        self._star_system_id: int = _parse.pss_int(mission_design_info.get("StarSystemId"))
        self._story_animation_id: int = _parse.pss_int(mission_design_info.get("StoryAnimationId"))
        self._story_description: str = _parse.pss_str(mission_design_info.get("StoryDescription"))
        self._weight: int = _parse.pss_int(mission_design_info.get("Weight"))

    @property
    def available_every_x_days(self) -> int:
        return self._available_every_x_days

    @property
    def available_from(self) -> _datetime:
        return self._available_from

    @property
    def available_to(self) -> _datetime:
        return self._available_to

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def chance(self) -> int:
        return self._chance

    @property
    def condition(self) -> str:
        return self._condition

    @property
    def exploration_percentage(self) -> int:
        return self._exploration_percentage

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def is_single_play(self) -> bool:
        return self._is_single_play

    @property
    def max_attempts_per_day(self) -> int:
        return self._max_attempts_per_day

    @property
    def max_ship_level(self) -> int:
        return self._max_ship_level

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def min_duration_since_last_event(self) -> int:
        return self._min_duration_since_last_event

    @property
    def min_ship_level(self) -> int:
        return self._min_ship_level

    @property
    def mission_description(self) -> str:
        return self._mission_description

    @property
    def mission_design_id(self) -> int:
        return self._mission_design_id

    @property
    def mission_design_status(self) -> str:
        return self._mission_design_status

    @property
    def mission_design_type(self) -> str:
        return self._mission_design_type

    @property
    def mission_title(self) -> str:
        return self._mission_title

    @property
    def required_mission_design_id(self) -> int:
        return self._required_mission_design_id

    @property
    def requirement_description(self) -> str:
        return self._requirement_description

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def star_system_id(self) -> int:
        return self._star_system_id

    @property
    def story_animation_id(self) -> int:
        return self._story_animation_id

    @property
    def story_description(self) -> str:
        return self._story_description

    @property
    def weight(self) -> int:
        return self._weight

    def _key(self):
        return (
            self.available_every_x_days,
            self.available_from,
            self.available_to,
            self.background_sprite_id,
            self.chance,
            self.condition,
            self.exploration_percentage,
            self.flags,
            self.is_single_play,
            self.max_attempts_per_day,
            self.max_ship_level,
            self.metadata,
            self.min_duration_since_last_event,
            self.min_ship_level,
            self.mission_description,
            self.mission_design_id,
            self.mission_design_status,
            self.mission_design_type,
            self.mission_title,
            self.required_mission_design_id,
            self.requirement_description,
            self.requirement_string,
            self.star_system_id,
            self.story_animation_id,
            self.story_description,
            self.weight,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AvailableEveryXDays": self.available_every_x_days,
                "AvailableFrom": self.available_from,
                "AvailableTo": self.available_to,
                "BackgroundSpriteId": self.background_sprite_id,
                "Chance": self.chance,
                "Condition": self.condition,
                "ExplorationPercentage": self.exploration_percentage,
                "Flags": self.flags,
                "IsSinglePlay": self.is_single_play,
                "MaxAttemptsPerDay": self.max_attempts_per_day,
                "MaxShipLevel": self.max_ship_level,
                "Metadata": self.metadata,
                "MinDurationSinceLastEvent": self.min_duration_since_last_event,
                "MinShipLevel": self.min_ship_level,
                "MissionDescription": self.mission_description,
                "MissionDesignId": self.mission_design_id,
                "MissionDesignStatus": self.mission_design_status,
                "MissionDesignType": self.mission_design_type,
                "MissionTitle": self.mission_title,
                "RequiredMissionDesignId": self.required_mission_design_id,
                "RequirementDescription": self.requirement_description,
                "RequirementString": self.requirement_string,
                "StarSystemId": self.star_system_id,
                "StoryAnimationId": self.story_animation_id,
                "StoryDescription": self.story_description,
                "Weight": self.weight,
            }

        return self._dict
